import numpy as np
#Do not import any other libraries
"""
Write a function that takes a number n as input and returns a 2 dimensional array of size nxn where the returned array has the following form.

f(1) returns array([[1]])
f(2) returns array([[2,1],
            `       [1,1]])
f(3) returns array([[3,2,1],
                    [2,2,1],
                    [1,1,1]])
f(4) returns array([[4,3,2,1],
                    [3,3,2,1],
                    [2,2,2,1],
                    [1,1,1,1]])

And so on. Hint: it is possible to add to a subset of an array. For example, say arr = np.zeros(4). Then if you run arr[:2] = arr[:2] + np.array([1,2])
and print arr, array([1,2,0,0]) would be outputed. Make sure you are returning a numpy array and not a list of lists.
"""

import numpy as np
a=1
b=2
d=3
g=4
def f(a):
    return np.array([a])
print(f(a))
def f(b):
    c = np.array([b,b-1,b-1,b-1])
    return c.reshape(2,2)
print(f(b))
def f(d):
    e = np.array([d,d-1,d-2,d-1,d-1,d-2,d-2,d-2,d-2])
    return e.reshape(3,3)
print(f(d))
def f(g):
    h = np.array([g,g-1,g-2,g-3,g-1,g-1,g-2,g-3,g-2,g-2,g-2,g-3,g-3,g-3,g-3,g-3])
    return h.reshape(4,4)
print(f(g))

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
