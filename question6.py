import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Write a function that takes a path to a text file as input and returns a pandas dataframe consisting of the entries in the text file. The elements in the
text file will be space separated, and the data in the file will not have a column header. The column names of the returned dataframe should take the form
column_1, column_2, ..... , column_N where N is the number of columns in the dataset. For example there is a file in this repository called test_data.txt.
Depending on where in your computer you downloaded the repository, there will be a specific path to that file which you can save to a string called path.
Then, f(path) should return the dataframe,

         column_1  column_2 column_3
    0        a         1        i
    1        b         2       ii
    2        c         3      iii
    3        d         4       iv
    4        e         5        v
"""
path="test_data.txt"
def f(path):
    df = pd.read_csv(path, header=None, delimiter=" ")
    return df.rename(columns={0:"column_1", 1:"column_2", 2:"column_3"})
print(f(path))
    ###########END CODE###############

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
