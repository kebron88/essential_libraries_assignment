import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#Do not import any other libraries

"""
Write a function that takes a path to a csv file as input. It will load this file into a pandas dataframe. This dataset is assumed to have a column called 'Class'.
We are going to create a classification model from scikit-learn to try to predict this class column. This function will need to take the following steps,

* Load the csv file specified in the path to a pandas dataframe.
* Remove all rows with missing values.
* Split the data into a training set and testing set with the sklearn train_test_split() method
(see https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). y is the 'Class' column, and X is all of the other columns. Use
a test_size of 0.3, and a random_state of 0. These values are important for when the assignment is graded.
* Initialize a scikit-learn logistic regression model and fit the model to the training set data.
(see https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html). Do not specify any hyperparameters.
* Return the classification score when predicted on the testing set data with the score() method.

There is a file called breast-cancer-wisconsin.csv in this repo (slightly modified from the original dataset in the UCI machine learning repository). Running f(path)
where path is the path to this csv file should return a score somewhere between 0.9 and 0.95.
"""
path = pd.read_csv("breast-cancer-wisconsin.csv")
def f(path):
    df = path.dropna()
    from sklearn.model_selection import train_test_split
    y = df["Class"]
    X = df[["Clump Thickness", "Uniformity of Cell Size", "Uniformity of Cell Shape", "Marginal Adhesion", "Single Epithelial Cell Size", "Bare Nuclei", "Bland Chromatin", "Normal Nucleoli", "Mitoses"]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)
print(f(path))
    ###########END CODE###############

if __name__=='__main__':
    ######CREATE TEST CASES HERE######
    pass
    ##################################
