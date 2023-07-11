#!/usr/bin/env python
# coding: utf-8

# **Vedant Modak**
#   | BE(IT) undergrad @ PES Modern College of Engineering,Pune

# **Calculating Efficient Frontier of a Portfolio**

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


# In[8]:


df.rename(columns={"VWAP": "HDFCVWAP"}, inplace=True)


# In[9]:


df.head()


# In[5]:


df1=pd.read_csv('F:\Data Analytics\Portfolio\Projects\Project - 6 (Stock Market Analysis)\ICICIBANK.csv')


# In[6]:


df1.head()


# In[7]:


df1.set_index('Date')


# In[10]:


df1.rename(columns={"VWAP": "ICICIVWAP"}, inplace=True)


# In[11]:


df1.head()


# In[14]:


df2=pd.concat([df['HDFCVWAP'], df1['ICICIVWAP']], axis=1, keys=['HDFC', 'ICICI'])


# In[15]:


df2.head()


# In[16]:


(df2/df2.iloc[0]*100).plot(figsize=(10,5))


# In[17]:


log_returns=np.log(df2/df2.shift(1))


# In[18]:


log_returns.mean()*250


# In[19]:


log_returns.cov()*250


# In[20]:


log_returns.corr()


# **Lets Consider a portfolio having these 2 securities with random weights**

# In[21]:


arr=np.random.random(2)
arr


# In[22]:


arr[0]+arr[1]


# **Considering 100% allocation of funds**

# In[23]:


weights=np.random.random(2)
weights /=np.sum(weights)
weights


# In[24]:


weights[0]+weights[1]


# **Expected Portfolio Return**

# In[25]:


np.sum(weights*log_returns.mean())*250


# **Expected Portfolio Variance**

# In[26]:


np.dot(weights.T, np.dot(log_returns.cov()*250, weights))


# **Expected Portfolio Volatality**

# In[27]:


np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights)))


# **Lets Check 1000 possible combinations of the assets for this porfolio**

# In[29]:


pfolio_returns=[]
pfolio_volatality=[]

for x in range(1000):
    weights=np.random.random(2)
    weights /=np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatality.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights))))
    
pfolio_returns, pfolio_volatality


# In[30]:


pfolio_returns=[]
pfolio_volatality=[]

for x in range(1000):
    weights=np.random.random(2)
    weights /=np.sum(weights)
    pfolio_returns.append(np.sum(weights*log_returns.mean())*250)
    pfolio_volatality.append(np.sqrt(np.dot(weights.T, np.dot(log_returns.cov()*250, weights))))

pfolio_returns=np.array(pfolio_returns)
pfolio_volatality=np.array(pfolio_volatality)

pfolio_returns, pfolio_volatality


# In[31]:


portfolios=pd.DataFrame({'Returns': pfolio_returns, 'Volatality': pfolio_volatality})


# In[32]:


portfolios.head()


# In[33]:


portfolios.tail()


# In[34]:


portfolios.plot(x='Volatality', y='Returns', kind='scatter', figsize=(10,6))
plt.xlabel('Expected Volatality')
plt.ylabel('Expected Return')

