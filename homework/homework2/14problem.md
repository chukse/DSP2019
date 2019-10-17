

```python
import numpy as np

np.iinfo(np.int32)
```




    iinfo(min=-2147483648, max=2147483647, dtype=int32)




```python
np.iinfo(np.int16)
```




    iinfo(min=-32768, max=32767, dtype=int16)




```python
a = np.iinfo(np.int16)
print(a.max)
```

    32767



```python
i = "1000000000"

maxInt16 = np.int16(a.max) +1



```


```python
print(maxInt16)
type(maxInt16)
```

    32768





    numpy.int64




```python
##Problem 14

"""
Using the numpy built in functions, it seems that the integer is automatically updated to 
int64 after an integer that is higher than the max has been reached.
"""

```
