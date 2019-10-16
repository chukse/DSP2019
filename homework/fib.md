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


   


    print(getfib(n_int))
