

```python
#Problem 6 Monte Carlo for Distribution

import random as r
import math as m
import numpy as np
import matplotlib.pyplot as plt

in_curve = 0
nsim = 1000 

x = np.linspace(0.001,15,100)

fig,ax=plt.subplots()

def formula(x): 
    return ((x+1)/12)*np.exp(-(x-1)**2/2./x)


y = formula(x)

ax.plot(x,y)


h = .2

square_x = np.random.rand(10000)*15

square_y = 

"""
for i in range(0,nsim):
    rand = r.random()
    
    x = r.random()**2
    y = ((rand + 1)/12)np.exp(-((rand - 1)**2)/(2*rand))    
    
    if m.sqrt(x + y) < .2:
        in_curve += 1


pi = (float(in_curve) / nsim) * 4

print(pi)

"""
```




    '\nfor i in range(0,nsim):\n    rand = r.random()\n    \n    x = r.random()**2\n    y = ((rand + 1)/12)np.exp(-((rand - 1)**2)/(2*rand))    \n    \n    if m.sqrt(x + y) < .2:\n        in_curve += 1\n\n\npi = (float(in_curve) / nsim) * 4\n\nprint(pi)\n\n'




![png](output_0_1.png)



```python

```
