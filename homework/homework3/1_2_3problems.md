

```python
##Problem 1



def is_even(n):
    return True if n%2 == 0 else False 
    
```


```python
is_even(3)
```




    False




```python
##Problem 2


def findMaxVal(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        max = findMaxVal(list[1:])
        return max if max > list[0] else list[0]
        
```


```python
findMaxVal([1,2,-3,4.5,2,-1])
```




    4.5




```python
##Problem 3


def findMaxValMaxLoc(list):
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]
    else:
        max = findMaxValMaxLoc(list[1:])
        count ++ ,return max if max > list[0] else list[0]
    
        
```


      File "<ipython-input-13-96bc4867aa80>", line 11
        count ++ ,return max if max > list[0] else list[0]
                 ^
    SyntaxError: invalid syntax
    



```python

```
