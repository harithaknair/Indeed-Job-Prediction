#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import warnings
from sklearn.feature_extraction.text import CountVectorizer
warnings.filterwarnings('ignore')
from nltk.corpus import stopwords
import re
import numpy as np
import pickle


# In[ ]:


# 1. Read the csv file which consists of the X_test data with the filename 'filename.csv' The Job Description is present in the 'text' column of the 'filename.csv' file


# In[ ]:


data = pd.read_csv('filename.csv', names = ['text'], header = 0 )


# In[ ]:


# 2. The data preprocessing of the Job Description is done and stored in a corpus which is run through CountVectorizer which converts the data which is given as an input to Pickled_Model which is our Machine Learning model


# In[ ]:



corpus = []

for i in range(len(data['text'])):  

    review = re.sub('[^a-zA-Z]', ' ', data['text'][i])
    review = review.lower()
    review = re.sub('data sci[a-z]+', '', review)
    review = re.sub('data eng[a-z]+', '', review)
    review = re.sub('software eng[a-z]+', '', review)
    
    review = review.split()
    review = ' '.join(review)
    corpus.append(review)


# In[ ]:


cv = CountVectorizer(max_features = 100)
X_test = cv.fit_transform(corpus).toarray()


# In[11]:


Pkl_Filename = "Pickle_Model.pkl"  


# In[15]:


with open(Pkl_Filename, 'rb') as file:  
    Prediction_Model = pickle.load(file)


# In[14]:


answers = Prediction_Model.predict(X_test)


# In[ ]:


# 3. The predictions of the model are stored in a numpy.ndarray called 'answers' which is converted  into a list called 'pred'  


# In[ ]:


pred = answers.tolist()


# In[ ]:


# 2 - Software Engineer
# 1 - Data Scientist
# 0 - Data Engineer


# In[ ]:


# 3. The Model's prediction list is converted the respective Job Ttiles i.e. Data Scientist, Data Engineer and Software Engineer


# In[ ]:


Job = []

for i in pred:
    
    if i == 0:
        Job.append("Data Engineer")
    
    elif i == 1:
        Job.append("Data Scientist")
        
    else:
        Job.append("Software Engineer")
        


# In[ ]:


# 4. The prediction list 'Job' is converted into a Dataframe 'df' and then into a csv file 'Prediction_output.csv'


# In[ ]:


d = {'Job Title': Job}


# In[ ]:


df = pd.DataFrame(data = d)


# In[ ]:


df.to_csv('Prediction_output.csv', index=False)


# In[ ]:


dd['Job Title'].value_counts()

