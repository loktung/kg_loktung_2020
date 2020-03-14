#CASE1: s1=abc s2=bcd print True a->b b->c c->d
#CASE2: s1=foo s2=bar print False f->b o->a o->
#^o already map to a cannot map to another character
#CASE3: s1=bar s2=foo print True b->f a->o r->o
#^a map to o and r map to o (Is not like o map to a and r)
#Only for 3 characters string

#!/usr/bin/env 
from sys import argv
#pass argument

def split(s1):
#Split s1 into characters
    charlist=list(s1)
    firstchar=charlist[0]
#The [0] as the first character
    x=1
#x=1 charlist[1] is the second character
    while x < len(charlist):
        if firstchar != charlist[x]:
            #if the first and second character does not match
            x=x+1#move to the next character
            #do nothing
        else:
            return False
    if charlist[1]!=charlist[2]: #compare the second and the third char
        return True
    else:
        return False

#argv[0] ->filename
s1=argv[1]
s2=argv[2]
#Ask user to input two string

print(split(s1))
#call function
    
        
   
