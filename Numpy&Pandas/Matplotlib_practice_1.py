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


# # scatter plot

# In[5]:


n = 1024

x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
t = np.arctan2(y, x)  # for color value

# scatter
plt.scatter(x, y, s = 75, c = t, alpha = 0.5)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.xticks(())   # hide x axis value
plt.yticks(())   # hide y axis value
plt.show()


# # bar chart

# In[11]:


# bar chart

n = 12
x = np.arange(n)
y1 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(x, + y1, facecolor = '#9999ff', edgecolor = 'white')
plt.bar(x, - y2, facecolor = '#ff9999', edgecolor = 'white')

# add annotation
for i in range(len(x)):
    # ha stands for horizontal alignment
    plt.text(x[i], y1[i] + 0.05, '%.2f' % y1[i], ha='center', va='bottom')


for i in range(len(x)):
    plt.text(x[i], -y2[i] - 0.05, '- %.2f' % y2[i], ha='center', va='top')
    
plt.xlim(-5, n)
plt.ylim(-1.25, 1.25)

# hide x and y ticks
plt.xticks(())
plt.yticks(())

plt.show()


# # contours

# In[14]:


# the height function
def f(x, y):
    return (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)

# filling contours
plt.contourf(X, Y, f(X, Y), 8, cmap = plt.cm.hot)

# add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors = 'black', linewidths = 0.5)

# add labels
plt.clabel(C, inline = True, fontsize = 10)

# hide x and y ticks
plt.xticks(())
plt.yticks(())

plt.show()


# In[19]:


# image

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
plt.imshow(a, interpolation = 'nearest', cmap = 'bone', origin = 'lower')

# add colorbar
plt.colorbar(shrink = 0.9)

# hide x and y ticks
plt.xticks(())
plt.yticks(())

plt.show()


# In[29]:


# 3D image

# import 3D model
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # Updated way to add a 3D subplot

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)

# height value
Z = np.sin(R)

# Surface plot with stride and custom colormap
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))

# Contour plot beneath the surface plot with 'rainbow' colormap
# 'zdir' indicates which axis to project onto, 'offset' is the z position for the contour
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))

# Setting the limits for the z-axis
ax.set_zlim(-2, 2)

plt.show()


# ## Subplot

# In[30]:


plt.figure()

# subplot 1
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

# subplot 2
plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 1])

# subplot 3
plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 1])

# subplot 4
plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 1])

plt.show()


# In[32]:


plt.figure()

# subplot 1
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

# subplot 2
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])

# subplot 3
plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])

# subplot 4
plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 1])

plt.show()


# ## subplot 2 grid

# In[36]:


plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan = 3, rowspan = 1)
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax_title')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan = 2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan = 2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.show()


# ## gridspec

# In[38]:


# import gridspec model
import matplotlib.gridspec as gridspec

plt.figure()

gs = gridspec.GridSpec(3, 3)

ax1 = plt.subplot(gs[0, :])

ax2 = plt.subplot(gs[1, :2])

ax3 = plt.subplot(gs[1:, 2])

ax4 = plt.subplot(gs[-1, 0])

ax5 = plt.subplot(gs[-1, -2])

plt.show()


# ## subplots

# In[40]:


f, ((ax11, ax12), (ax21, ax22)) =plt.subplots(2, 2, sharex = True, sharey = True)
ax11.scatter([1, 2], [1, 2])

plt.show()


# ## image in image

# In[46]:


# import gridspec model
import matplotlib.gridspec as gridspec

fig = plt.figure()

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.xlabel('y')


plt.show()


# ## primary and secondry axis

# In[50]:


x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color = 'g')
ax1.set_ylabel('Y2', color = 'b')

plt.show()


# ## animation

# In[54]:


# import anamation model
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig = fig, func = animate, frames = 100, init_func = init, interval = 20, blit = False )

plt.show()


# In[ ]:





# In[ ]:




