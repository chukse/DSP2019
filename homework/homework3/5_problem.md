

```python
#Problem 5A

import random 
import numpy as np 
import matplotlib.pyplot as plt 

def doRandomWalk(nstep,startPosition):
    prob = [0.5, 0.5]
    positions = [startPosition]
    rand = np.random.random(nstep)
    back = rand < prob[0] 
    forward = rand > prob[1] 
    
    for i_back, i_forward in zip(back, forward): 
        r_back = i_back and positions[-1] > 1
        r_forward = i_forward and positions[-1] < 4
        positions.append(positions[-1] - r_back + r_forward)
    
    return positions[-1]
    
    
```


```python
doRandomWalk(10,-10)
```




    -6




```python
#Problem 5B and 5C

def simulateRandomWalk(nsim,nstep,startPosition):
    list = []
    
    for i in range(0,nsim):
        list.append(doRandomWalk(nstep,startPosition))
    
    #return list
    
    plt.hist(list) 
    plt.show() 

    
```


```python
simulateRandomWalk(10000,10,-10)
```


![png](output_3_0.png)



```python

```


```python

```
