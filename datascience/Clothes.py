#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[113]:


pip install -U scikit-learn scipy matplotlib


# In[143]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

Clothes_data= pd.read_csv('Clothes.csv')
X = Clothes_data.drop(columns = ['prefer'])
y = Clothes_data['prefer']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# In[136]:


# model = DecisionTreeClassifier()


# In[145]:


model.fit(X,y)

tree.export_graphviz(model, out_file = 'clothes-recommender.dot', 
                    feature_names=['age', 'gender'],
                    class_names =sorted(y.unique()),
                    label = 'all',
                    rounded=True,
                    filled=True)
#joblib.dump(model, 'clothes-recommender.joblib')
#model = joblib.load('clothes-recommender.joblib')
#predictions = model.predict([[56,0]] )
#predictions


# In[131]:


#model.fit(X_train,y_train)
#predictions = model.predict(X_test )
#score =accuracy_score(y_test, predictions)
#score


# In[134]:





# In[ ]:





# In[ ]:





# In[ ]:




