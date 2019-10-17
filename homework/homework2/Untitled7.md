

```python
a = 5
b = a
print (id(a), id(b))
 
c = b
b = 3
print (a,b,c)
print (id(a),id(b),id(c))
 
b = a
b = 5
print (id(a), id(b))
```

    4491642400 4491642400
    5 3 5
    4491642400 4491642336 4491642400
    4491642400 4491642400



```python
##Problem 2A:
"""
In the first 3 lines of code, a is set to 5 and b is set to a.
The identity of each variable is then printed with its "unique" integer.
Since b = a, the identity should print out the same integer.

In the next 4 lines, c is set to equal to b and b is updated to equal 3.
The variables a,b,c are then printed to give 5 3 5.
Since c = b before updating, c should have the same unique integer as a, and b should now have new unique integer.

In the next 3 lines, b is reverted back to being set to a. After this, b is then updated to the integer 5.
Therefore, the id for b and a should be the same since they are both equal to the same integer.
"""

```




    '\nIn the first 3 lines of code, a is set to 5 and b is set to a.\nThe identity of each variable is then printed with its "unique" integer.\nSince b = a, the identity should print out the same integer.\n\nIn the next 4 lines, c is set to equal to b and b is updated to equal 3.\nThe variables a,b,c are then printed to give 5 3 5.\nSince c = b before updating, c should have the same unique integer as a, and b should now have new unique integer.\n\nIn the next 3 lines, b is reverted back to being set to a. After this, b is then updated to the integer 5.\nTherefore, the id for b and a should be the same since they are both equal to the same integer.\n'




```python
a = [5]
b = a
print (id(a), id(b))
 
b.append(1)
print (a,b)
print (id(a),id(b))
```

    4530199688 4530199688
    [5, 1] [5, 1]
    4530199688 4530199688



```python
##Problem 2b:

"""
Initiate a list with just one element 5.
declare b as equal to the list a.
The identity of b and a will be the same.
After appending element 1 to be, since they are the same unique number,
they will both update to [5,1]
"""
```




    '\nProblem 2b:\n\nInitiate a list with just one element 5.\ndeclare b as equal to the list a.\nThe identity of b and a will be the same.\nAfter appending element 1 to be, since they are the same unique number,\nthey will both update to [5,1]\n'




```python
a = [5]
b = list(a)
print (a,b)
print (id(a), id(b))
 
b = a[:]
print (a,b)
print (id(a), id(b))
```

    [5] [5]
    4529560008 4530570952
    [5] [5]
    4529560008 4529560584



```python
##Problem 2c:

"""
Problem 2c:

a is set as a list with 5.
b is set to create new a new storage list with a's elements.

Therefore, the first print statement will show a and b as having the same content but the second print statement shows that these two lists have different unique identities.

b is then set the copy of list a.
Lists in Python are immutable objects, so a new memory storage is allocated for variable b. 
Therefore in the next print statement, b has a different unique value and a stays the same.
"""
```




    "\nProblem 2c:\n\na is set as a list with 5.\nb is set to create new a new storage list with a's elements.\n\nTherefore, the first print statement will show a and b as having the same content but the second print statement shows that these two lists have different unique identities.\n\nb is then set the copy of list a.\nTherefore in the next print statement, b has a different unique value and a stays the same.\n"




```python
a = (5,)
b = tuple(a)
print (id(a), id(b))
 
b = a[:]
print (id(a), id(b))
```

    4529436600 4529436600
    4529436600 4529436600



```python
##Problem 2d:

"""
Because a is set to a tuple with 5 in it, and b is set to a tuple of a, which is already a tuple, a and b 
have the same unique when printed out.

Variable b is then updated to be a new object that is a copy of the tuple a. However, because tuples are immutable, 
a new reference is made rather than a new object, therefore the unique value of b will be the same as a.
```
