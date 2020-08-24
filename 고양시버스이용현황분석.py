#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data_bus_station = pd.read_csv("20.고양시_버스정류소.csv")


# In[4]:


data_bus_station2 = data_bus_station


# In[5]:


data_bus_user = pd.read_csv("21.버스_정류장별_승하차_정보.csv")


# In[6]:


data_bus_user2=data_bus_user


# In[13]:


bus_data=pd.merge(data_bus_station2, data_bus_user, how='inner',
                  on=['STATION_NM','STATION_ID'])


# In[14]:


bus_data.head(5)


# In[15]:


bus_data.tail(5)


# In[18]:


bus_data2=bus_data.sort_values(by="GETON_CNT", ascending=False)


# In[19]:


bus_data2.head(5)


# In[20]:


bus_data2.tail(5)


# In[27]:


bus_del = bus_data2[bus_data2['GETON_CNT']==0].index
bus_data3=bus_data2.drop(bus_del)


# In[28]:


bus_data3.head(3)


# In[30]:


bus_data3.tail(3)


# In[33]:


bus_data3.info()


# [20.버스정류소 데이터]와 [21.버스_정류장별_승하차_정보] 데이터를 merge
# 승차인원수에 따라 정렬
# 승차인원(GETON_CNT)=0 index 제외

# In[32]:


bus_data3.describe()


# In[35]:


bus_data3.head(15)


# 버스마다 승하차 지점이 약간씩 차이가 남.
# 하지만 버스정류장 이름은 동일함.

# In[ ]:




