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


ril_data['simple_return']=(ril_data['Average Price']/ ril_data['Average Price'].shift(1))-1
print (ril_data['simple_return'])


# In[6]:


ril_data['simple_return'].plot(figsize=(8,5))
plt.show()


# In[7]:


average_return_a= ril_data['simple_return'].mean()*248
print (average_return_a)


# In[8]:


print (str(round(average_return_a,5) *100)+'%')

