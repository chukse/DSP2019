while (True):

    n = input("Please enter a non-negative integer or type stop: ")
    
    if n == 'stop': break
        
    if n.isalpha() == True:
        print("The input argument is not a non-negative integer! \n")
        continue
    
    else:
        n_int = int(n)
        
        print(type(n_int))
                    
    
    

        
    def getfib(n_int):
        
        answer = 0
        if n_int < 0:
            print("The input argument is not a non-negative integer! \n")
            return 
        

        elif n_int==0: answer = 0
        elif n_int==1: answer = 1
        

        else:
            for i in range(0, n_int):
            
                answer += getfib((n_int-1)+getfib(n_int-2))
        
        return answer
    
    
    print(getfib(n_int))
    
        
      
