#!/usr/bin/env python
# coding: utf-8

# ## Volumetric Rendering

# In this exercise you will use some basic methods of visualizing medical volumes. A CT volume will be loaded for you into numpy array - do not worry too much about file format, what the pixel values are, and the libraries used to load the image - we will get to it in the lessons that follow.

# In[3]:


import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import scipy.ndimage as nd


# In[5]:


img = nib.load("data/volume.nii.gz")


# In[6]:


img_np = img.get_fdata()
img_np.shape


# At this point img_np is a numpy 3D array that contains our medical volume, its size is 360 x 360 x 330.
# 
# The first dimension is the X axis, and if we slice the array across it, we will get slices in sagittal plane. The second dimension is the Y axis, and slicing across it will get us the coronal plane. Third dimension is the Z axis and if we slice across it we will get the axial plane. This is a common way of assigning axes to a medical image. Again, in later lessons we will talk in more detail about patient coordinate systems and axes.
# 
# Let's visualize a sagittal slice number 100. Remember the Multi-planar reconstruction task we've talked about in the lectures? This is exactly what we are going to do here - for our CT volume, the axial plane is the primary one, and we are reconsructing a cut across a plane orthogonal to the primary one.
# 
# Note that we specify the grayscale colormap for matplotlib as this is the method of choice for visualizing medical images.

# In[7]:


plt.imshow(img_np[100,:,:], cmap="gray")


# ## Orthographic projection

# In[8]:


vr = np.zeros((img_np.shape[1], img_np.shape[2]))

for i in range(img_np.shape[0]):
    img = img_np[i,:,:]
    vr += img


# In[14]:


plt.imshow(nd.rotate(vr,90),cmap='gray')


# ## Maximum Intensity Projection
# Another popular method of rendering 3D volumes is called "Maximum Intensity Projection". This method makes sure that maximum values (in case of CT corresponding to the densest structures) are propagated and prominently visualized. A MIP projection can help a physician visualize foreign materials, bones or structures filled with a contrast medium.
# 
# You will create a MIP projection in this task.

# In[20]:


# For a change, let's stack slices along the Y axis and thus visualize the coronal plane
mip = np.zeros((img_np.shape[0], img_np.shape[2]))

# TASK: write same loop you wrote above (but going through the Y-axis), but now rather than adding all values, use 
# np.maximum function to save the maximum value of each pixel across our entire slice stack



for i in range(img_np.shape[1]):
    mip = np.maximum(mip,img_np[:,i,:])
    


# In[22]:


plt.imshow(nd.rotate(mip,90),cmap='gray')

