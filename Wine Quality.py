#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df=pd.read_csv("winequality-red.csv.")


# In[3]:


df.head()


# In[4]:


print(df.columns)
print(df.shape)


# In[5]:


df.info()


# In[6]:


df.describe().T


# In[7]:


df.nunique()


# In[8]:


df.duplicated().sum()


# In[9]:


plt.figure(figsize = (15,15))
sns.heatmap(df.corr(),annot=True, cmap= 'PuBuGn')


# In[10]:


color = sns.color_palette("pastel")

fig, ax1 = plt.subplots(3,4, figsize=(24,30))
k = 0
columns = list(df.columns)
for i in range(3):
    for j in range(4):
            sns.distplot(df[columns[k]], ax = ax1[i][j], color = 'red')
            k += 1
plt.show()

