#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

# In[29]:


plt.figure(num = 3, figsize = (8,5))  #figsize(width, hight)

## setting legend
l1, = plt.plot(x, y2, label = 'up')
l2, = plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--', label = 'down')
plt.legend(handles = [l1, l2], labels = ['aaa', 'bbb'], loc = 'best')

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


# In[12]:


x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# Setting annotation
x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s = 50, color = 'b')
plt.plot([x0, x0], [y0, 0], 'k--', lw = 2.5)

# method 1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# method 2
plt.text(-3.7, 3, r'$This is the some text. \mu\ \sigma_i\ \alpha_t $',
        fontdict = {'size':16, 'color':'red'})

plt.show()


# In[15]:


# tick transparecy

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
plt.plot(x, y, linewidth=10, zorder=1)      # set zorder for ordering the plot in plt 2.0.2 or higher
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

#method 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'white', edgecolor = 'None', alpha = 0.7))

plt.show()


# In[ ]:




