

```python
#Problem 7


import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt

Door = {1:True,2:False,3:False}
nsim = 100000
def trial(switch, Door):
    

    Doorlist = list(Door)
    #NumWinBySwitching = np.zeros(nsim)
    #NumWinByNotSwitching = np.zeros(nsim)
    
    
    guessChoice = rnd.choice(Doorlist)
   
    if switch:
        if guessChoice == 3:
            hostChoice = 2
    
        else: 
            hostChoice = 3 
    
        doors_left = [num for num in range(1,len(Doorlist))
                           if num not in (guessChoice, hostChoice)]
    
        guessChoice = rnd.choice(doors_left)


    return guessChoice == 1
    
  
```


```python
def multiple_trials(nsim, switch, Door):


    wins = 0
    
    for i in range(nsim):
        
        
        if trial(switch, Door):
            
            wins += 1
    
    
    return wins


wins_without_switching = multiple_trials(nsim, False, Door)

wins_with_switch = multiple_trials(nsim, True, Door)

print('Proportion of wins without switching {}'.format(wins_without_switching/nsim))

print('Proportion of wins with switching {}'.format(wins_with_switch/nsim))


```

    Proportion of wins without switching 0.33464
    Proportion of wins with switching 0.66793
    


```python

```


```python

```


```python

```
