#ke@cerebras.net

# for testing
import numpy as np

#use N-D python arrays for prototyping. (cpp vectors for production)

def shape(a):
    """
    gives shape of array. This should be converted to a privated variable to reduce calculation
    """
    if type(a)!=list:
        return tuple()
    return (len(a),) + shape(a[0])

def rank(a):
    return len(shape(a))

def add_with_boardcasting(a,b):
    """
    add with broadcasting, like numpy
    return None if broadcasting is not allowed
    """

    # base case which is when both items are numbers
    if type(a)!=list and type(b)!=list:
        return a+b

    # ensure b is the one with less rank to be padded
    if rank(b)>rank(a):
        a,b=b,a

    dimension_diff = rank(a)-rank(b)
    padding =(1,)* (dimension_diff )
    a_shape = shape(a)
    b_shape = padding+ shape(b)
    for i,j in zip(a_shape,b_shape):
        if (i!=1 and i!=j and j!=1):
            #CANNOT BROADCAST
            return None

    # wrap b into the same shape as b_shape
    for i in range(dimension_diff):
        b=[b]

    result_shape = tuple([ max(i,j) for i,j in zip(a_shape,b_shape) ])


    n=result_shape[0]

    result = [0]*n # make the result as a 1*n vector

    # 0 if this dim has single elemenent, otherwise 1
    b_is_const = b_shape[0]==n
    a_is_const = a_shape[0]==n 

    for i in range(n): 
        result[i] = add_with_boardcasting(a[i*a_is_const],b[i*b_is_const])
    
    return result


print(add_with_boardcasting(
    [1,2,3],
    [[10],[20],[30]]
))


def unit_test():
    tests = {
        'arr3' : [1,2,3],
        'arr3x3' : [
            [10,10,10],
            [20,20,20],
            [30,30,30]
        ],
        'arr3x2' : [
            [10,170,102],
            [26,208,230],
        ],
        'arr3x1' : [
            [17], 
            [25], 
            [33]
        ],
        'arr1x1':[
            [11], 
        ],
        'arr1':[3],
        'arr':5,
        'arr5x4':np.random.randint(1, 100, size=(5,4)).tolist(),
        'arr4':np.random.randint(1, 100, size=(4,)).tolist(),
        'arr15x3x5':np.random.randint(1, 100, size=(15,3,5)).tolist(),
        'arr15x1x5':np.random.randint(1, 100, size=(15,1,5)).tolist(),
        'arr3x1':np.random.randint(1, 100, size=(3,1)).tolist(),
        'arr3x5':np.random.randint(1, 100, size=(3,5)).tolist(),
    }

    def unit_test_shape(array_dict):
        for name, arr in array_dict.items():
            if shape(arr)!=np.array(arr).shape:
                print("ERROR in shape:", name,arr)
    unit_test_shape(tests)

    def unit_test_add(array_dict):
        for name, arr in array_dict.items():
            for name2, arr2 in tests.items():
                result =np.array(add_with_boardcasting(arr,arr2))
                try:
                    reference = np.array(arr)+np.array(arr2)
                except:
                    reference = None
                if not np.array_equal(reference,result):
                    print(name,name2,reference)
        for i in range(1000):
            num_dimensions = np.random.randint(1, 6)
            shape1 = tuple(np.random.randint(1, 7, size=num_dimensions))
            arr = np.random.randint(1, 100, size=shape1).tolist()

            num_dimensions = np.random.randint(1, 6)
            shape2 = tuple(np.random.randint(1, 7, size=num_dimensions))
            arr2 = np.random.randint(1, 100, size=shape2).tolist()
            result =np.array(add_with_boardcasting(arr,arr2))
            try:
                reference = np.array(arr)+np.array(arr2)
            except:
                reference = None
            if not np.array_equal(reference,result):
                print(name,name2,reference)
    unit_test_add(tests)

unit_test()