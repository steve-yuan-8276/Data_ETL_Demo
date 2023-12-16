#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s = pd.Series([1, 3, 6, np.nan, 44, 2])
print(s)


# In[4]:


dates = pd.date_range('20231215', periods = 6)
print(dates)


# In[9]:


df = pd.DataFrame(np.random.randn(6,4), index = dates, columns = ['a', 'b', 'c', 'd'])
print(df)


# In[10]:


df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)


# In[14]:


df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20231215'),
    'C':pd.Series(1, index = list(range(4)), dtype = 'float32'),
    'D':pd.array([3] * 4, dtype='int32'),
    'E':pd.Categorical(["test", "train", "power", "man"]),
    'F':'foo'
})

print(df2)


# In[15]:


df2.index


# In[17]:


df2.columns


# In[19]:


df2.values


# In[21]:


df2.describe()  #only consider number


# In[22]:


df2.T  #pivot table


# In[23]:


df2.sort_index(axis = 1, ascending = False)


# In[24]:


df2.sort_index(axis = 0, ascending = False)


# In[28]:


df2.sort_values(by = 'E', ascending = False)


# ## Select data

# In[29]:


dates = pd.date_range('20231215', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, columns = ['A','B','C','D'])

print(dates)
print(df)


# In[31]:


print(df['A'], df.A)


# In[32]:


print(df[0:3])  # select by index


# In[33]:


print(df['2023-12-15':'2023-12-17'])  # select by keys


# In[34]:


print(df.loc['20231215'])  # select by label


# In[36]:


print(df.loc[:, ['A','B']])  #select by label (rows and column)


# In[37]:


print(df.iloc[3:5, 1:3])   #select by position


# In[38]:


print(df.iloc[[1,3,5], 1:3])


# In[39]:


print(df[df.A > 8])  # select by indexing


# In[40]:


df.iloc[2,2] = 111
print(df)


# In[42]:


df.A[df.A > 4] = 0  # set column A's value to zero when A > 4
print(df)


# In[48]:


df['E'] = np.random.random(6)
print(df)


# ## Non-value

# In[49]:


df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)


# In[50]:


print(df.dropna(axis = 0, how = 'any'))   # how could be "any", 'All'


# In[51]:


print(df.dropna(axis = 1, how = 'any'))   


# In[52]:


print(df.fillna(value = 0))   set non-value to zero


# In[53]:


print(df.isnull())


# In[54]:


print(np.any(df.isnull()) == True)


# ## Combine DateFrame

# In[56]:


df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns = ['A','B','C','D'])

print(df1)
print(df2)
print(df3)


# In[59]:


# concatenating
# method 1
res = pd.concat([df1, df2, df3], axis = 0, ignore_index = True)
print(res)


# In[63]:


#join ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['A','B','C','D'], index = [1, 2, 3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['B','C','D','E'], index = [2, 3, 4])

print(df1)
print(df2)


# In[64]:


res = pd.concat([df1, df2], join = 'outer')  #default outer join
print(res)


# In[66]:


res = pd.concat([df1, df2], join = 'inner', ignore_index = True)  # like SQL join
print(res)


# In[72]:


res = pd.concat([df1, df2], axis = 1).reindex(df1.index)  #.reindex(df1.index) like left join in SQL

print(res)


# ## Merge dataframe

# In[76]:


left = pd.DataFrame({
    'key':['K0','K1','K3','K4'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})

right = pd.DataFrame({
    'key':['K0','K1','K3','K4'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

print(left)
print(right)


# In[78]:


res = pd.merge(left, right, on = 'key')
print(res)


# In[85]:


left = pd.DataFrame({
    'key1':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})

right = pd.DataFrame({
    'key2':['K0','K1','K3','K5'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

res = pd.merge(left, right, left_on='key1', right_on='key2', how = 'left', indicator = True)
print(res)


# ## matplotlib plots

# In[86]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[89]:


#Series
data = pd.Series(np.random.randn(1000), index = np.arange(1000))
data = data.cumsum()


# In[88]:


data.plot()
plt.show()


# In[92]:


# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4), index = np.arange(1000), columns = list('ABCD'))

data = data.cumsum()

print(data)


# In[93]:


data.plot()
plt.show()


# In[ ]:




