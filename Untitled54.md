

```python
from scipy.io import loadmat
import numpy as np
from scipy.stats import norm
from scipy.optimize import fmin
%matplotlib notebook
import matplotlib.pyplot as plt
from scipy.stats import gompertz
%matplotlib inline

# load MATLAB data file
cells= loadmat("cells.mat")
Data  = cells["cells"]

time = [0,10,12,14,16,18,20,22]

dy = .05
    
def getGompertz(Data,la, c):
    time = Data[3]
    la = Data[0]
    c = Data[1]
    initial_N = 100000

    getGompertz = np.sum( np.log(initial_N * exp(la*abs(1-exp(-c*time)))) );
    
    return getGompertz


Parameters = fmin   ( func = getGompertz  \
                     , x0 = Data)     \
                    
print( "mean = {}, standard-deviation = {}".format(Parameters[0],Parameters[1]) )
    
    
    
#plt.errorbar(Data[3], Data[0], yerr=dy);





for i in range(Data.shape[3]):
    
    for j in range(len(time)):
        fig.suptitle('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment.'.format(time[i]))    
    
    fig, ax = plt.subplots(nrows=4, ncols=4, sharex=True, sharey=True)
    #ax.set_yscale('log')
    #ax.set_xscale('log')
    ax[0][0].title.set_text('z = 1')
    ax[0][0].imshow(Data[:,:,1,i])
    
    ax[0][1].title.set_text('z = 2')
    ax[0][1].imshow(Data[:,:,2,i])
    
    ax[0][2].title.set_text('z = 3')
    ax[0][2].imshow(Data[:,:,3,i])
    
    ax[0][3].title.set_text('z = 4')
    ax[0][3].imshow(Data[:,:,4,i])
    
    ax[1][0].title.set_text('z = 5')
    ax[1][0].imshow(Data[:,:,5,i])
    
    ax[1][1].title.set_text('z = 6')
    ax[1][1].imshow(Data[:,:,6,i])
    
    ax[1][2].title.set_text('z = 7')
    ax[1][2].imshow(Data[:,:,7,i])
    
    ax[1][3].title.set_text('z = 8')
    ax[1][3].imshow(Data[:,:,8,i])
    
    ax[2][0].title.set_text('z = 9')
    ax[2][0].imshow(Data[:,:,9,i])
    
    ax[2][1].title.set_text('z = 10')
    ax[2][1].imshow(Data[:,:,10,i])
    
    ax[2][2].title.set_text('z = 11')
    ax[2][2].imshow(Data[:,:,11,i])
    
    ax[2][3].title.set_text('z = 12')    
    ax[2][3].imshow(Data[:,:,12,i])
    
    ax[3][0].title.set_text('z = 13')    
    ax[3][0].imshow(Data[:,:,13,i])
    
    ax[3][1].title.set_text('z = 14')
    ax[3][1].imshow(Data[:,:,14,i])
    
    ax[3][2].title.set_text('z = 15')    
    ax[3][2].imshow(Data[:,:,15,i])
    #ax[3][3].imshow(Data[:,:,16,i])    
    


    



#print(Data[:,:,10,1])

# fig = plt.figure( figsize=(4.5, 4) \
#                 , dpi= 150 \
#                 , facecolor='w' \
#                 , edgecolor='w' \
#                 ) # create figure object
# ax = fig.add_subplot(1,1,1) # Get the axes instance

# plt.hist(Data)
# print (len(Data))
# plt.show()
```


    ---------------------------------------------------------------------------

    MemoryError                               Traceback (most recent call last)

    <ipython-input-94-d83f9efff47e> in <module>
         28 
         29 Parameters = fmin   ( func = getGompertz  \
    ---> 30                      , x0 = Data)     \
         31 
         32 print( "mean = {}, standard-deviation = {}".format(Parameters[0],Parameters[1]) )
    

    ~\Anaconda3\lib\site-packages\scipy\optimize\optimize.py in fmin(func, x0, args, xtol, ftol, maxiter, maxfun, full_output, disp, retall, callback, initial_simplex)
        414             'initial_simplex': initial_simplex}
        415 
    --> 416     res = _minimize_neldermead(func, x0, args, callback=callback, **opts)
        417     if full_output:
        418         retlist = res['x'], res['fun'], res['nit'], res['nfev'], res['status']
    

    ~\Anaconda3\lib\site-packages\scipy\optimize\optimize.py in _minimize_neldermead(func, x0, args, callback, maxiter, maxfev, disp, return_all, initial_simplex, xatol, fatol, adaptive, **unknown_options)
        516         N = len(x0)
        517 
    --> 518         sim = numpy.zeros((N + 1, N), dtype=x0.dtype)
        519         sim[0] = x0
        520         for k in range(N):
    

    MemoryError: 



```python

```


```python

```


```python

```
