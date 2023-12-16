#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


array = np.array([[1,2,3],
                  [2,3,4]])


# In[5]:


print(array)


# In[6]:


array.ndim


# In[7]:


array.shape


# In[8]:


array.size


# In[14]:


a = np.array([2,3,4],dtype = np.int64)
print(a)
print(a.dtype)


# In[16]:


b = np.array([2,3,4],dtype = np.float64)
print(a)
print(b.dtype)


# In[17]:


c = np.zeros((3,4))
print(c)


# In[19]:


d = np.ones((3,4), dtype = np.int64)
print(d)


# In[20]:


e = np.empty((3,4))
print(e)


# In[21]:


f = np.arange(10, 20, 2)
print(f)


# In[22]:


g = np.arange(12).reshape((3,4))
print(g)


# In[23]:


h = np.linspace(1,10,25)
print(h)


# In[29]:


i = np.linspace(1,10,24).reshape((8,3))
print(i)


# ## Basic Calculation

# In[30]:


m = np.array([10, 20, 30, 40])
n = np.arange(4)
print(m)
print(n)


# In[31]:


a = m - n
print(a)


# In[32]:


b = m + n
print(b)


# In[33]:


c = n ** 2
print(c)


# In[35]:


d = np.sin(m) * 10
print(d)


# In[36]:


print(n < 3)


# In[37]:


print(n == 3)


# In[39]:


m = np.array([[1,1],
              [0,1]])
n = np.arange(4).reshape(2,2)
print(m)
print(n)


# In[40]:


a = m * n
print(a)


# In[41]:


b = np.dot(m, n)
print(b)


# In[42]:


c = m.dot(n)
print(c)


# In[43]:


m = np.random.random((2,4))
print(m)


# In[47]:


a = np.sum(m)
b = np.max(m, axis = 1) #row
c = np.min(m, axis = 0) #column
print(a,b,c)


# In[48]:


m = np.arange(2,14).reshape((3,4))
print(m)


# In[49]:


a = np.argmin(m)
print(a)


# In[50]:


b = np.argmax(m)
print(b)


# In[51]:


c = np.mean(m)
print(c)


# In[52]:


d = np.average(m)
print(d)


# In[53]:


e = np.median(m)
print(e)


# In[54]:


f = np.cumsum(m) #runing total
print(f)


# In[55]:


g = np.diff(m)  #Calculate the diffrence between number and previse number
print(g)


# In[56]:


h = np.nonzero(m) #return the index of non-zero element
print(h)


# In[57]:


i = np.sort(m)
print(i)


# In[60]:


j = np.transpose(m)  #pivot table
print(m)
print(j)


# In[61]:


k = np.clip(m, 5, 9)
print(k)


# In[63]:


m = np.arange(3,15)
print(m)


# In[64]:


a = m[3]
print(a)


# In[65]:


n = np.arange(3,15).reshape(3,4)
print(n)


# In[69]:


b = n[2] # 2 is index of row
print(b)


# In[70]:


c = n[1][1]
print(c)


# In[71]:


d = n[1,1]
print(d)


# In[72]:


for row in n:   # print each row number
    print(row)


# In[74]:


print(n.T)  # print each column number, you need pivot table first


# In[75]:


for column in n.T:   
    print(column)


# In[78]:


e = n.flatten()
print(e)


# In[80]:


for item in n.flat:
    print(item)


# ## combine array

# In[3]:


m = np.array([1,1,1])
n = np.array([2,2,2])
print(m,n)


# In[5]:


c = np.vstack((m,n))   #vertical stack
print(c)


# In[7]:


print(m.shape)
print(n.shape)
print(c.shape)


# In[8]:


e = np.hstack((m,n))  # horizontal stack
print(e)
print(e.shape)


# In[11]:


f = m[np.newaxis, :]
print(f)


# In[12]:


g = m[: , np.newaxis]
print(g)


# In[14]:


h = np.concatenate((m,n,m))
print(h)


# In[19]:


i = np.concatenate((m,n,m,n), axis = 0)   #When working with 1D arrays, you can only concatenate them along axis 0
print(i) 


# ## split array

# In[20]:


m = np.arange(12).reshape((3,4))
print(m)


# In[22]:


a = np.split(m, 2, axis = 1)  #split by column
print(a)


# In[24]:


b = np.split(m, 3, axis = 0)  #split by row
print(b)


# In[25]:


c = np.array_split(m, 3, axis = 1)
print(c)


# In[27]:


d = np.vsplit(m, 3)
e = np.hsplit(m, 4)
print(d)
print(e)


# ## Copy & deep copy

# In[28]:


a = np.arange(4)
print(a)


# In[35]:


b = a
c = a
d = b


# In[34]:


b is a


# In[36]:


a[0] = 5
print(a)


# In[37]:


c is a


# In[38]:


d is a


# In[39]:


b = a.copy()   #deep copy
print(b) 


# In[40]:


a is b


# In[ ]:




