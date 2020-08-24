#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


s_station = pd.read_csv("29.지하철 역별 이용객수.csv")


# In[7]:


s_station.head(8)


# In[5]:


s_station.isnull().sum()


# In[6]:


s_station.info()


# In[ ]:


# 지하철 역별 총 승하차 고객
# 일 평균 승하차 인원
# 일 이용 총 인원

for i in range(len(s_station['승하차구분'])):
    if s_station['승하차구분'].iloc[i]=='총 승하차':
        
        

