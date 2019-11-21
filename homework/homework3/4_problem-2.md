

```python
#Problem 4 Monte Carlo for PI

import random as r
import math as m

in_curve = 0
nsim = 1000 

for i in range(0,nsim):
    x = r.random()**2
    y = r.random()**2
    
    if m.sqrt(x + y) < 1.0:
        in_curve += 1

pi = (float(in_curve) / nsim) * 4

print(pi)
```

    3.144



```python

```
