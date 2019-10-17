

```python
numbers = list(range(10))
print(numbers)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
for n in numbers:
    i = len(numbers)//2
    del numbers[i]
    print ('n={}, del {}'.format(n,i), numbers)
```

    n=0, del 5 [0, 1, 2, 3, 4, 6, 7, 8, 9]
    n=1, del 4 [0, 1, 2, 3, 6, 7, 8, 9]
    n=2, del 4 [0, 1, 2, 3, 7, 8, 9]
    n=3, del 3 [0, 1, 2, 7, 8, 9]
    n=8, del 3 [0, 1, 2, 8, 9]



```python
##Problem 15

"""
This weird is behavior is because the list in of itself is being modified by deleting 1 number each iteration. 
This causes the scope of the loop to update by removing 1 each iteration. 
The list then deletes an intger in the loop based on its position that is calculated by the equation.
The specific integer iteration in the list, deletion position, and list are then printed each iteration. 
In n = 1 and n = 2, they are the same because integers are being divided and therefore the remainder is ignored and the whole integer is processed.
So, in n = 1, 9/2 is calculated to be 4 which is stored in i,and the number of the position of i is deleted, which is 4.
In, n =2, 8/2 is calculated to be 4 as well, and now the number in position 4 is 5 because the list is updated without 4 being in it.
5 is then deleted and the list is printed.

In n = 3, the list is update to only have 6 positions now, and 3 - 6 have been deleted out of position. Therefore, the next list item is 7. 
The loop then goes to integer 7 in the list and 6/2 is calculated to be 3. Position 3 in the list is then deleted which is 7 and the scope of the list is now 4 
which allows the loop to end.

"""
```
