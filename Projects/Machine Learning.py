#!/usr/bin/env python
# coding: utf-8

# In[18]:


from sklearn import datasets
import pandas as pd, numpy as np

data = pd.read_csv("1_county_level_confirmed_cases.csv")

#deleted entries with missing values
data = data.dropna()



print(data.keys())


# In[19]:


data["NCHS_urbanization"]


# In[20]:


data["deaths"]


# In[25]:


from sklearn import model_selection as ms
from sklearn import svm
from sklearn.metrics import accuracy_score


for i in range(20):
    #randomly split the data into training and testing
    X_train, X_test, y_train, y_test = ms.train_test_split(data.deaths, data.NCHS_urbanization, test_size=0.1)

    X_train, X_val, y_train, y_val = ms.train_test_split(data.deaths, data.NCHS_urbanization, test_size=0.11)
    #.11 * .9 = .099, closest to .1



    #got error, "ValueError: Expected 2D array, got 1D array instead" so doing the suggested reshape
    X_train = np.array(X_train)
    X_train =X_train.reshape(-1, 1)

    X_test = np.array(X_test)
    X_test =X_test.reshape(-1, 1)

    #creating a model, and training it

    clf = svm.SVC(kernel='linear')
    clf.fit(X_train, y_train)
    
    
    


# In[26]:


from sklearn.metrics import accuracy_score

# having the model predict/guess the classes for the test data

pred_y = clf.predict(X_test)

# generating an accuracy score 

#1 ACCURACY
print("Accuracy score:", accuracy_score(pred_y, y_test))


# In[27]:


#feature weights

print(clf.coef_)


# In[28]:


from sklearn.metrics import classification_report

#get precision and recall values
print(classification_report(y_test, pred_y))


# The very low accuracy, precision, recall scores, and feature weights tell us that this machine learning model does not work very well. The precision and recal improved after running 20 times, but is still very low.
