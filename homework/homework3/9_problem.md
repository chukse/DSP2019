

```python
import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd 

year = []
month = []
anomaly = []
anomaly1 = []
a = []
mynumbers = []
year_month = []
with open('usaTemperatureHistory.txt','r') as f:
    for _ in range(70):
        next(f)  
    for line in f:
        mynumbers = line.split('    ')
        year.append(mynumbers[0])
        month.append(mynumbers[1])
        anomaly.append(mynumbers[2])
        
for line in anomaly:
    if line.startswith('   NaN') == False:
        a = line.split()
    
        anomaly1.append(a[0])

def stringToFloatList(list):
    
    float_x = []
    for i in list:
        double_x = float(i)
        float_x.append(double_x)
    
    return float_x

year_x = stringToFloatList(year)
month_x = stringToFloatList(month)
anomaly1_y = stringToFloatList(anomaly1)



year_month = [(year + month)/13 for year, month in zip(year_x, month_x)]


x = np.array(year_month)
y = np.array(anomaly1_y)
x1 = np.linspace(0, 1, 3239)
x2 = np.linspace(0, 1, 3167)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x,y)



plt.show()
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-63-2205155e7309> in <module>
         49 fig = plt.figure()
         50 ax = fig.add_subplot(1,1,1)
    ---> 51 ax.plot(x,y)
         52 
         53 


    //anaconda3/lib/python3.7/site-packages/matplotlib/axes/_axes.py in plot(self, scalex, scaley, data, *args, **kwargs)
       1664         """
       1665         kwargs = cbook.normalize_kwargs(kwargs, mlines.Line2D._alias_map)
    -> 1666         lines = [*self._get_lines(*args, data=data, **kwargs)]
       1667         for line in lines:
       1668             self.add_line(line)


    //anaconda3/lib/python3.7/site-packages/matplotlib/axes/_base.py in __call__(self, *args, **kwargs)
        223                 this += args[0],
        224                 args = args[1:]
    --> 225             yield from self._plot_args(this, kwargs)
        226 
        227     def get_next_color(self):


    //anaconda3/lib/python3.7/site-packages/matplotlib/axes/_base.py in _plot_args(self, tup, kwargs)
        389             x, y = index_of(tup[-1])
        390 
    --> 391         x, y = self._xy_from_xy(x, y)
        392 
        393         if self.command == 'plot':


    //anaconda3/lib/python3.7/site-packages/matplotlib/axes/_base.py in _xy_from_xy(self, x, y)
        268         if x.shape[0] != y.shape[0]:
        269             raise ValueError("x and y must have same first dimension, but "
    --> 270                              "have shapes {} and {}".format(x.shape, y.shape))
        271         if x.ndim > 2 or y.ndim > 2:
        272             raise ValueError("x and y can be no greater than 2-D, but have "


    ValueError: x and y must have same first dimension, but have shapes (3239,) and (3167,)



![png](output_0_1.png)



```python

```
