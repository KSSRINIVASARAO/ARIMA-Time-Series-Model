#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# Here I am Importing all the neccessary libraries that i can use 
# 
# PANDAS- To Upload files and read the content of files
# 
# NUMPY- Numpy as you know updated for mathematical problems
# 
# MATPLOTLIB and SEABORN- For plotting graphs that related to data.

# In[4]:


data=pd.read_csv(r"E:\Data Analysis\DATA FILES\international-airline-passengers.csv",skipfooter=2)

Here by using pd.read_csv i am reading the file international-airline-passengers from the location that i had in my computer and here i am using skipfooter to avoid unrelated data
# In[5]:


data.head()


# Here is the header of the data from international-airline-passengers 

# In[6]:


data.tail()


# Here is the tail or end contents of the data from international-airline-passengers to make sure no unwanted
# data is prescent at the bottom

# In[7]:


data.info()


# Data.info() shows the information about data the columns name data having data type and total rows

# In[8]:


data["Month"]=pd.to_datetime(data["Month"])


# pd.to_datetime used to specify Specify a date parse order if arg is str or its list-likes.

# In[9]:


df=data.drop("Month",axis=1)
df.columns=["volume"]
df.index=data["Month"]
df.head()


# Dropping month from the columns
# and assigning volume (volume of passangers) in data columns 
# indexing the month 

# In[10]:


plt.plot(df)
plt.show()


# plotting the data which timevarient

# In[11]:


rolling_mean=df.rolling(10).mean()
rolling_sd=df.rolling(10).std()
plt.plot(rolling_mean)
plt.plot(rolling_sd)
plt.show()


# Using rolling mean and standard deviation on data check the data how variation is happening

# In[12]:


from statsmodels.tsa.stattools import adfuller
adfuller(df["volume"])


# pvalue>0.5 null hypothesis is not standard and it is stationary 
# pvalue<0.05 null hyphotesis is stationary
# Using aduller method here can see the that pvalue>0.05 its around 0.8 so data is still not stationary

# In[13]:


dflog=np.log(df)
plt.plot(dflog)
plt.show()


# Using Numpy Log is applying on data to get the result as same but here its shows the log of mean and standard deviation is or small variation is there

# In[14]:


dflog=dflog-dflog.shift(1)
dflog.head()


# Using Numpy Log and shift is applying on data to get the result similar to but not the same as the gross return calculated by pct_change()

# In[15]:


rolling_mean1=dflog.rolling(10).mean()
rolling_sd1=dflog.rolling(10).std()
plt.plot(rolling_mean1)
plt.plot(rolling_sd1)
plt.show()


# Applying mean and std deviation to check my data after log function usage and now its 
# showing the data is not varient but little more constant

# In[16]:


from statsmodels.tsa.stattools import adfuller
adfuller(dflog["volume"].dropna())


# pvalue>0.5 null hypothesis is not standard and it is stationary 
# pvalue<0.05 null hyphotesis is stationary
# Using aduller method here can see the that pvalue>0.05 its around -2.717 so data is stationary

# In[23]:


from statsmodels.tsa.stattools import acf,pacf
ac=acf(dflog.dropna())
plt.plot(ac)
plt.grid()
plt.show()
pac=pacf(dflog.dropna())
plt.plot(pac)
plt.grid()
plt.show()


# Assigning ACF(Aauto-correlation Function) and PACF(Partial Auto-Correlation Function) plots 

# In[24]:


from statsmodels.tsa import arima_model
arima=arima_model.ARIMA(df,(2,1,2))
model=arima.fit()


# ARIMA(p,d,q)=ARIMA(2,1,2)
# p is the number of autoregressive terms,
# d is the number of nonseasonal differences needed for stationarity, and
# q is the number of lagged forecast errors in the prediction equation.

# In[25]:


model.plot_predict(start=1,end=204)


# In[ ]:




