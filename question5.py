import numpy as np
#Do not import any other libraries
"""
Write a function that takes 2 two dimensional arrays arr1 and arr2, and returns another two dimensional array. The resulting array should have the rows of
arr2 where the first element of each row is greater than zero, concatenated underneath the rows of arr1 where the first element of each row is greater than
zero. So for example, suppose

arr1 = array([[1,2,3.5,4],
              [3,-2,0,7],
              [0,8,-1,0]])

and arr2 = array([[-3,9,8.4,-11],
                  [0.5,-1,-1,-1],
                  [2,11,-3,-2.4]])

Then f(arr1,arr2) should return array([[ 1. ,  2. ,  3.5,  4. ],
                                       [ 3. , -2. ,  0. ,  7. ],
                                       [ 0.5, -1. , -1. , -1. ],
                                       [ 2. , 11. , -3. , -2.4]])
"""

arr1 = np.array([[5.5,8,7,-7], [-2.2,9.8,6.3,-7.7], [0,1.2,3.,4], [8.1,4.2,11.,1.]])
arr2 = np.array([[-4.5,6.,7.1,9.],[1.9,4.,6.6,-3.2], [-2.2,5.7,-9.2,13], [1.1,5.,7.9,9.9]])

def f(arr1,arr2):
    a = arr1[arr1[:,0]>0,:]
    b = arr2[arr2[:,0]>0,:]
    return np.concatenate((a,b) )
print(f(arr1,arr2))
    ###########END CODE###############

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
