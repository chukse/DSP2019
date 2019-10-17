

```python
def get_triangle_area(vertices):
    b = abs((vertices[1][0]*vertices[2][1])-(vertices[2][0]*vertices[1][1])-
            (vertices[0][0]*vertices[2][1])+(vertices[2][0]*vertices[0][1])+(vertices[0][0]*vertices[1][1])-
            (vertices[1][0]*vertices[0][1]))
    a = (1/2)*b
    return a 
    
```


```python
def test_get_triangle_area():
    """
    Verify the area of a triangle with vertex coordinates
    (0,0), (1,0), and (0,2).
    """
    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1, v2, v3]
    expected = 1
    computed = get_triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = 'computed area=%g != %g (expected)' % (computed, expected)
    assert success, msg
    print (computed) 
```


```python
print(test_get_triangle_area())
```

    1.0
    None
    


```python

```
