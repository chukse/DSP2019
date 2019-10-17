#!/usr/bin/env python
# coding: utf-8

# In[3]:


from time import process_time

while (True):
    n = input("Please enter a non-negative integer or type stop: ")

    if n == 'stop': break
    
    if n.isalpha() == True:
        print("The input argument is not a non-negative integer! \n")
        continue

    else:
        n_int = int(n)
    
    
                


    def fibloop(n):
   
        fib_list=[0,1]
        if n>1:
            fibOld = 0
            fibCurrent = 1
            
            for i in range(2,n+1):
                fibNew = fibCurrent +fibOld
                fibOld = fibCurrent 
                fibCurrent = fibNew
            
                a=fib_list[i-1]+fib_list[i-2]
                fib_list.append(a)
            
            return a
        if n==0 or n==1: return n
    
    
    
    t1_start = process_time()
    a = fibloop(n_int)
    t1_stop = process_time()
    
    print("fib({}) = {}".format(n_int, a))
    print("Average Runtime: {}".format((t1_stop-t1_start)))
    


# In[ ]:




