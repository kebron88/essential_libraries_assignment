import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Suppose you have created a regression model to predict some quantity. Write a function that takes 2 numpy arrays that both have the same length, y and y_pred.
The function should return the loss between the predicted and the actual values where the losss function is defined here to be

loss = 1/N * Sum from i=1 to N  (y[i] - y_pred[i])**2    (See sklearn part 1 video for explanation of this loss function)

Where N is the number of datapoints. For example if y = array([0.5,1,2,4,8]) and y_pred = array([1,2,3,4,5]), then f(y, y_pred) should return 2.25
"""
y = np.array([4,11.5,6,3,8])
y_pred = np.array([7.1,12,5,6.5,5])
def f(y,y_pred):
    N=len(y)
    return np.sum((y-y_pred)**2)/N
print(f(y,y_pred))
    ###########END CODE###############

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
