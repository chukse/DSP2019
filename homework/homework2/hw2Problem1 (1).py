import platform
print("This is python version " + platform.python_version() + "\n")


s = "Python is the best language for String manipulation!"
print(s + "\n")

backwards = s[::-1]

print(backwards + "\n")

skipOneBackwards = s[::-2]

print(skipOneBackwards + "\n")

def lower_upper(s):
    new = ""
    for i in s:
        if(i.isupper() == True):
            new += (i.lower())
            
        elif(i.islower() == True):
            new += (i.upper())
            
            
        else:
            new += i

    
    return new


        
print(lower_upper(s) + "\n")
   


def a(s):
    count_a = 0
    count_A = 0
    for i in s:
        if(i == 'a'):
            count_a += 1
        elif(i == 'A'):
            count_A += 1
        
    return count_A,count_a

countA,counta = a(s)
print('The sentence \'{}\' contains'.format(s) + "\n" + '{} \'a\' letters, and'.format(counta) + "\n" + '{} \'A\' letters!'.format(countA)+ "\n")



def linebreak(s):
    new = ''
    for i in s:
        if(i.isspace() == True):
            new += i
            new += "\n"
        else:
            new += i
            
    return new


print(linebreak(s) + "\n")

lowerCase_linebreak = linebreak(s)

type(lowerCase_linebreak)

print(lowerCase_linebreak.upper() + "\n")