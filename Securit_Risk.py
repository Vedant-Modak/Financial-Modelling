#!/usr/bin/env python
# coding: utf-8

# **Vedant Modak**
#   | BE(IT) undergrad @ PES Modern College of Engineering,Pune.

# **Calculating Security's Risk with Standard deviation**

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('F:\Data Analytics\Portfolio\Projects\Project - 6 (Stock Market Analysis)\HDFC.csv')


# In[3]:


df.head()


# In[4]:


df.set_index('Date')


# **Calculating Log Returns**

# In[5]:


df['log_return']=np.log(df['Close']/df['Close'].shift(1))
print (df['log_return'])


# In[6]:


df['log_return'].std()


# In[7]:


df['log_return'].std()*250**0.5

