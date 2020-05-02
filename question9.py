import numpy as np
import pandas as pd
#Do not import any other libraries

"""
Write a function that takes a pandas dataframe, df as input. df is assumed to have a column called 'text' where each entry is a block of text.
The function should return all the rows in df where the number of words in the 'text' entry is greater than or equal to 10. Hint: it is possible
to define a function within another function and then use that function locally. There is a csv file called testdf9.csv. Loading this as a
dataframe and running f(df) should return

                                                text
1  played between two opposing teams who take tur...
3  when a player on the fielding team, called the...
4  throws a ball which a player on the batting te...
6  is to hit the ball into the field of play, all...
7  having them advance counter-clockwise around f...
"""
df = pd.read_csv("testdf9.csv")

def f(df):
    def L10(s):
        x = s.split()
        if len(x)>=10:
            return True
        else:
            return False
    return df[df["text"].apply(L10)]
print(f(df))
    ###########END CODE###############

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
