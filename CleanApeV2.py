
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

df.to_csv('ape1.csv')

df.ix[:, 'datetime'] = pd.to_datetime(df['datetime'], format="%Y-%m-%d %H:%M:%S")
df.ix[:, 'app_type'] = df['app_categories'].apply(listcolumn)

df['installed'] = df['installed'].apply(TrueFalse)

# df['installed'].unique()

# strange_index = df[np.logical_and(
#         np.logical_and(
#             df['app_type'] == 'games',
#             df['installed']),
#         ~df['clicked'])].index

df['weekday'] = df['datetime'].map(lambda x: x.isoweekday())
df['hours'] = df['datetime'].map(lambda x: x.hour)

df['app_type2'] = df['app_type'].astype('category')

df['app_type2'].unique()

df_filter = df[['weekday', 'hours', 'app_type2', 'os', 'country', 'impression', 'clicked', 'installed2']]

testf = df_filter.groupby(['weekday', 'hours']).sum()

testf

testf['installed2'].plot()

fig = plt.figure(figsize=(20, 10))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(1, 7):
    plt.plot(testf.loc[i]['installed2'], linewidth=2.0, label=days[i-1])
plt.legend()

test_cat = df_filter.groupby(['app_type2']).sum()
print test_cat

test_cat.fillna(0)

fig = plt.figure(figsize=(20, 10))
for i in range(1, 7):
    plt.plot(testf.loc[i][''], linewidth=2.0, label=days[i-1])
plt.legend()

df_filter[np.logical_and(
        np.logical_and(
            df_filter['app_type2'] == 'games',
            df_filter['installed2']),
        ~df_filter['clicked'])]
