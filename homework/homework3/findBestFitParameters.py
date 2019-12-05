#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!python
#!/usr/bin/env python
get_ipython().run_line_magic('matplotlib', 'notebook')
from scipy.io import loadmat
import numpy as np
from scipy.stats import norm
from scipy.optimize import fmin


# load MATLAB data file
Drand = loadmat("Drand.mat")
Data  = Drand["Drand"]


import matplotlib.pyplot as plt
fig = plt.figure( figsize=(4.5, 4)                 , dpi= 150                 , facecolor='w'                 , edgecolor='w'                 ) # create figure object
ax = fig.add_subplot(1,1,1) # Get the axes instance

plt.hist(Data)
print (len(Data))
plt.show()

# find the parameters of Gaussian distribution

def getNegLogProbNorm(Param):
    avg = Param[0];
    std = Param[1];
    getNegLogProbNorm = - np.sum( np.log( norm.pdf(x = Data, loc = avg, scale = std) ) );
    return getNegLogProbNorm

Parameters = fmin   ( func = getNegLogProbNorm                      , x0 = np.array([1,10])                         )
print( "mean = {}, standard-deviation = {}".format(Parameters[0],Parameters[1]) )


# In[14]:





# In[ ]:


.9

