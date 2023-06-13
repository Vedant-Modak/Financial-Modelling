#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


ril_data =pd.read_csv('F:\Reliance_data.csv')


# In[3]:


ril_data.head()


# In[4]:


ril_data.set_index('Date')


# In[5]:


ril_data['log_return']=np.log(ril_data['Average Price']/ril_data['Average Price'].shift(1))
print (ril_data['log_return'])


# In[6]:


average_log_return=ril_data['log_return'].mean()*248
print (average_log_return)


# In[7]:


print (str(round(average_log_return,5)*100)+'%')

