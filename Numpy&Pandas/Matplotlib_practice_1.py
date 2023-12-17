#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


x = np.linspace(-3, 3, 50)
y1 = x * 2 + 1

print(x, y)


# In[6]:


plt.figure()
plt.plot(x, y1)
plt.show()


# In[13]:


y2 = x ** 2
plt.figure(num = 3, figsize = (8,5))  #figsize(width, hight)
plt.plot(x, y2)
plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--')
plt.show()


# ## Modify X axis or Y axis

# In[23]:


plt.figure(num = 3, figsize = (8,5))  #figsize(width, hight)
plt.plot(x, y2)
plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--')

plt.xlim((-1, 2))  #setting X axis range
plt.ylim((-2, 3))
plt.xlabel('X Axis') # Setting label 
plt.ylabel('Y Axis')

new_ticks = np.linspace(-1, 2, 5)   #set x axis
plt.xticks(new_ticks)

plt.yticks(
    [-2, -1, 0, 1, 2, 3],
    ['awful', 'bad', 'not bad', 'nomal', 'good', 'very good']
)

#gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.show()


# In[ ]:




