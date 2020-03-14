#CASE1: s1=abc s2=bcd print True a->b b->c c->d
#CASE2: s1=foo s2=bar print False f->b o->a o->
#^o already map to a cannot map to another character
#CASE3: s1=bar s2=foo print True b->f a->o r->o
#^a map to o and r map to o (Is not like o map to a and r)

#!/usr/bin/env 
from sys import argv
#pass argument

def split(s1):
#Split s1 into elements
    charlist=list(s1)
    x=0
    y=1
#charlist[x] first element
    for x in range (0,(len(charlist)-1)):#go through each elements
        
        while y < len(charlist):#compare the first element with the rest  
            if charlist[x] != charlist[y]:
                #if the first and second character does not match
                y=y+1#move to the next character
                #do nothing
            else:
                return False
    if charlist[len(charlist)-1]!=charlist[len(charlist)-2]: #compare [-1]&[-2]
        return True
    else:
        return False

#argv[0] ->filename
s1=argv[1]
s2=argv[2]
#Ask user to input two string

print(split(s1))
#call function
    
        
   
