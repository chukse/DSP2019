

```

```


```
#Problem 6 Part A
from time import process_time

while (True):
    n = input("Please enter a non-negative integer or type stop: ")

    if n == 'stop': break
    
    if n.isalpha() == True:
        print("The input argument is not a non-negative integer! \n")
        continue

    else:
        n_int = int(n)
    
    
                


    def getfib(n):
   
        fib_list=[0,1]
        if n>1:
            f = getfib(n-1) + getfib(n-2)
            return f
    
        if n==0 or n==1: return n


   
    t1_start = process_time()
    a = getfib(n_int)
    t1_stop = process_time()
    
    print("fib({}) = {}".format(n_int, a))
    print("Average Runtime: {}".format((t1_stop-t1_start)))
    

```

    Please enter a non-negative integer or type stop: 0
    fib(0) = 0
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 1
    fib(1) = 1
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 2
    fib(2) = 1
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 3
    fib(3) = 2
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 4
    fib(4) = 3
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 8
    fib(8) = 21
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 10
    fib(10) = 55
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 15
    fib(15) = 610
    Average Runtime: 0.0
    Please enter a non-negative integer or type stop: 20
    fib(20) = 6765
    Average Runtime: 0.015625
    Please enter a non-negative integer or type stop: 25
    fib(25) = 75025
    Average Runtime: 0.046875
    Please enter a non-negative integer or type stop: 30
    fib(30) = 832040
    Average Runtime: 0.71875
    Please enter a non-negative integer or type stop: 35
    fib(35) = 9227465
    Average Runtime: 6.421875
    Please enter a non-negative integer or type stop: stop
    


```

```
