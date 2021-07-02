import math

def factors(n):
    c=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            c+=1
    c*=2
    if math.sqrt(n)%1==0:
        c-=1
    return c

i=0
val=0
while(1):
    val=val+i
    c=factors(val)
    if c>500:
        print(val)
        break
    i+=1
