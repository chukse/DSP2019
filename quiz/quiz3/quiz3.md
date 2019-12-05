

```python

get_ipython().run_line_magic('matplotlib', 'notebook')
from scipy.io import loadmat
import numpy as np
from scipy.stats import norm
from scipy.optimize import fmin


# load MATLAB data file
Drand = loadmat("Drand.mat")
Data  = Drand["Drand"]




def getSumDistanceSquared(mean):
    
    #getSumDistanceSquared = (-mean)**2
    
    getSumDistanceSqueared = sum( np.log( norm.pdf(x = Data, loc = mean,))**2    
    
    return getSumDistanceSquared

Parameters = fmin   ( func = getSumDistanceSquared, x0 = np.array([10])                         )
print( "mean = {}, standard-deviation = {}".format(Parameters) )
#print("Least-squares means = " + )
```


      File "<ipython-input-15-ca8012e32f38>", line 21
        return getSumDistanceSquared
             ^
    SyntaxError: invalid syntax
    



```python

```
