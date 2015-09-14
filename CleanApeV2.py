
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')


import numpy as np
import pandas as pd
import csv
import datetime
import matplotlib.pyplot as plt


# In[2]:

def listcolumn(x):
    x = x.translate(None, '"')
    x = x.translate(None, ' ')
    x = x[1:-1].split(",")
    j = x[-1]
    return j


# In[29]:

def TrueFalse(value):
    if value[0]=='F':
        value = False
    else:
        value = True
    return value


# In[40]:

reader = list(csv.reader(open('rtb_data.csv', 'rb'), delimiter='\t'))
colheaders = reader[0]

df = pd.DataFrame(reader[1:])

dffilter = df.iloc[:, 0:20]
dffilter.columns = [colheaders]

dffilter.to_csv('ape1.csv')


# In[41]:

df = pd.read_csv('ape1.csv')


# In[43]:

df['installed'].unique()


# In[52]:

df=df.drop(strange_index)


# In[54]:

df.to_csv('ape1.csv')


# In[50]:

df[np.logical_and(
        np.logical_and(
            df['app_type'] == 'games',
            df['installed']),
        ~df['clicked'])].index


# In[51]:

print strange_index


# In[48]:

df.ix[:, 'datetime'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S")
df.ix[:, 'app_type'] = df['app_categories'].apply(listcolumn)


# In[49]:

df['installed']=df['installed'].apply(TrueFalse)


# In[33]:

df['installed'].unique()
#df['installed2']=df['installed'].map({'True':True, 'False':False})


# In[8]:

df['installed2']=df['installed'].astype(bool)


# In[16]:

df.head()


# In[37]:

strange_index=df[np.logical_and(
        np.logical_and(
            df['app_type'] == 'games',
            df['installed']),
        ~df['clicked'])].index


# In[10]:

df['weekday'] = df['datetime'].map(lambda x: x.isoweekday())
df['hours'] = df['datetime'].map(lambda x: x.hour)


# In[11]:

df['app_type2']=df['app_type'].astype('category')


# In[12]:

df['app_type2'].unique()


# In[13]:

df_filter = df[['weekday', 'hours', 'app_type2', 'os', 'country', 'impression', 'clicked', 'installed2']]


# In[ ]:

x=np.where(df_filter['installed2']==True)
len(x[0])


# In[14]:

df_test=df_filter.iloc[0:20,:]


# In[15]:

df_test


# In[ ]:

testf=df_filter.groupby(['weekday', 'hours']).sum()


# In[ ]:

testf


# In[ ]:

testf['installed2'].plot()


# In[ ]:

fig=plt.figure(figsize=(20,10))
days=['Monday', 'Tuesday', 'Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
for i in range(1,7):
    plt.plot(testf.loc[i]['installed2'], linewidth=2.0, label=days[i-1])
plt.legend()


# In[ ]:

days[0]


# In[ ]:

test_cat=df_filter.groupby(['app_type2']).sum()
print test_cat


# In[ ]:

test_cat.fillna(0)


# In[ ]:

fig=plt.figure(figsize=(20,10))
for i in range(1,7):
    plt.plot(testf.loc[i][''], linewidth=2.0, label=days[i-1])
plt.legend()



# In[ ]:

df_filter[np.logical_and(
        np.logical_and(
            df_filter['app_type2'] == 'games',
            df_filter['installed2']),
        ~df_filter['clicked'])]


# In[ ]:
