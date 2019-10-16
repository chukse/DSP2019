

```python
import timeit as tt
def isPrime(n):
    
    isPrime = True
    
    def is_divisible(n,divisor):
        if n<(divisor-1)*divisor: return False
        if n%divisor==0: return True
        else:
            divisor += 1
            return is_divisible(n,divisor)

    if n==2:
        isPrime = True
    elif is_divisible(n,divisor=2):
        isPrime = False
    return isPrime

def getNumPrimes(n):
    count = 0
    if n == 1:
        return count
    else:
        n -= 1
        if isPrime(n):
            return getNumPrimes(n-1)
        else:
            return getNumPrimes(n-1) + 1
```


```python
%timeit getNumPrimes(13)
```

    5.91 µs ± 369 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
    


```python
import timeit as tt
while True:
    n = input("Please enter an integer ")
    if n == 'stop':
        break 
    
    if n.isalpha() == True:
        print("The input argument is not a non-negative integer! \n")
        continue

    else:
        n_int = int(n)
    
        print(type(n_int))  
    
    def isPrime_for(n):
        isprime = False
    
        for i in range(1,n):
            if i%2 == 0:
                isprime = True
            else:
                isprime = False
        
        return isprime 

    def get_prime_for(n):
           
        count = 0
        if n == 1:
            return count
        else:
            for i in range(0,n):
                if isPrime_for(i):
                    count += 1
                else:
                    continue
    
        #largestPrime = max(primeList)
        #return largestPrime
        return count 

    print(get_prime_for(n_int))
```

    Please enter an integer 13
    <class 'int'>
    5
    Please enter an integer 500
    <class 'int'>
    249
    Please enter an integer stop
    


```python
%timeit getNumPrimes(500)
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-13-b10c898e738b> in <module>
    ----> 1 get_ipython().run_line_magic('timeit', 'getNumPrimes(500)')
    

    ~\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py in run_line_magic(self, magic_name, line, _stack_depth)
       2311                 kwargs['local_ns'] = sys._getframe(stack_depth).f_locals
       2312             with self.builtin_trap:
    -> 2313                 result = fn(*args, **kwargs)
       2314             return result
       2315 
    

    <C:\Users\HP Owner\Anaconda3\lib\site-packages\decorator.py:decorator-gen-61> in timeit(self, line, cell, local_ns)
    

    ~\Anaconda3\lib\site-packages\IPython\core\magic.py in <lambda>(f, *a, **k)
        185     # but it's overkill for just that one bit of state.
        186     def magic_deco(arg):
    --> 187         call = lambda f, *a, **k: f(*a, **k)
        188 
        189         if callable(arg):
    

    ~\Anaconda3\lib\site-packages\IPython\core\magics\execution.py in timeit(self, line, cell, local_ns)
       1156             for index in range(0, 10):
       1157                 number = 10 ** index
    -> 1158                 time_number = timer.timeit(number)
       1159                 if time_number >= 0.2:
       1160                     break
    

    ~\Anaconda3\lib\site-packages\IPython\core\magics\execution.py in timeit(self, number)
        167         gc.disable()
        168         try:
    --> 169             timing = self.inner(it, self.timer)
        170         finally:
        171             if gcold:
    

    <magic-timeit> in inner(_it, _timer)
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         25             return getNumPrimes(n-1)
         26         else:
    ---> 27             return getNumPrimes(n-1) + 1
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    ... last 1 frames repeated, from the frame below ...
    

    <ipython-input-1-a7af6e01eec1> in getNumPrimes(n)
         23         n -= 1
         24         if isPrime(n):
    ---> 25             return getNumPrimes(n-1)
         26         else:
         27             return getNumPrimes(n-1) + 1
    

    RecursionError: maximum recursion depth exceeded in comparison



```python
%timeit get_prime_for(500)
```

    10.5 ms ± 664 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
    


```python
##The for loop implementation is significantly faster
```
