import numpy as np
from sklearn.naive_bayes import BernoulliNB

data = np.loadtxt(open("hw4-data.csv"), delimiter=",", skiprows=1)
X, Y = data[:,:-1], data[:,-1]

clf = BernoulliNB()
clf.fit(X, Y)
test_data = [[0, 1, 0, 0, 0],
             [0, 1, 1, 1, 0],
             [1, 0, 0, 0, 1]]
print(clf.predict_proba(test_data))

'''
RESULTS FOR NBC:

[[0.48543409 0.51456591] 1
 [0.65004491 0.34995509] 0
 [0.46844286 0.53155714]] 1

'''
