#ke@cerebras.net

# for testing
import numpy as np

# will be converted to cpp vectors  
arr1d = [1,2,3] # (3)
arr2d = [
    [10,10,10],
    [20,20,20],
    [30,30,30]
]

arr2d_2 = [[10], [20], [30]]  #(3,1)

def shape(a):
    """
    gives shape of array
    """
    if type(a)!=list:
        return tuple()
    return (len(a),) + shape(a[0])


def add_with_boardcasting(a,b,ashape,bshape,result,resultshape):
    pass
    #determine shape of a, b and compare them
    
    #lower rank array have shape padded with 1 in front
    
    # obtain the final shape by taking max() of each dim
    # intial this 1d vector/array
    # calculate index in flatten array 
    #(3,1)
    #(1,3)
    #(3,3)
    # if len(resultshape)==1:
    #     #basecase
    #     for i in range(resultshape[0]):
    #         result[startindex+i]=a[...]+b[...]
            
    # else:
    #     for i in range(resultshape[-2]): 
    #         startindex = # 
    #         add_with_boardcasting(a,b,ashape[:-1],bshape[:-1],result,resultshape[:-1],startindex)

    # pass


#print(np.array(arr2d)+np.array(arr1d))

print(np.array(arr2d_2)+np.array(arr1d))


"""
A      (2d array):  5 x 4
B      (1d array):      1
Result (2d array):  5 x 4

A      (2d array):  5 x 4
B      (1d array):      4
Result (2d array):  5 x 4

A      (3d array):  15 x 3 x 5
B      (3d array):  15 x 1 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 5
Result (3d array):  15 x 3 x 5

A      (3d array):  15 x 3 x 5
B      (2d array):       3 x 1
Result (3d array):  15 x 3 x 5
"""