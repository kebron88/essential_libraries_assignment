import numpy as np
#Do not import any other libraries
"""
Write a function that takes 2 one dimensional arrays and returns the cosine similarity between the arrays. The cosine similarity is defined as
the dot product between the 2 arrays where each array has been divided by its magnitude. The magnitude is the defined as the square root of the
sum of the squares of the elements. So the cosine similarity of arrays arr1 and arr2 is DotProduct(arr1/magnitude(arr1), arr2/magnitude(arr2)).
Round your answer to 4 decimal places. Suppose arr1 = array([1,2,3]) and arr2 = array([-4,0,3.5]). Then f(arr1, arr2) should return 0.3268
"""

import numpy as np
arr1 = np.array([2,6,8])
arr2 = np.array([-4,5,-2.5])

def f(arr1,arr2):
    a= arr1/np.linalg.norm(arr1)
    b=arr2/np.linalg.norm(arr2)
    return round(np.dot(a,b),4)
print(f(arr1,arr2))
    ###########END CODE###############

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
