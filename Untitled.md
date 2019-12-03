

```python
import numpy as np
import pandas as pd
#x_y = np.zeros((0,2))
x_values = []
y_values = []
import csv
with open('points.txt','r') as f:
    reader = csv.reader(f, delimiter = ',')
    for _ in range(1):
        next(f)  
  
    for row in reader:
        x_values.append(row[0])
        y_values.append(row[1])

sum =0

def stringToFloatList(list):
    
    float_x = []
    for i in list:
        double_x = float(i)
        float_x.append(double_x)
    
    
    return float_x


x_floatList = (stringToFloatList(x_values))

y_floatList = (stringToFloatList(y_values))

#np.append([x_y, [4, 5, 6]], [[7, 8, 9]], axis=0)
    
x_y = np.vstack((np.asarray(x_floatList),np.asarray(y_floatList))).T

print(x_y)




```

    [[9.34508557 8.63519067]
     [9.54974537 8.35831472]
     [9.48553116 8.59465695]
     ...
     [4.55786927 5.07288193]
     [4.65156079 5.10719972]
     [4.57620973 4.86047407]]



```python


```
