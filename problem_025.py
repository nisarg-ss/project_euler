term=2
a=1
b=1

while(True):
    c=a+b
    term+=1
    if len(str(c))==1000:
        print(term)
        break
    a=b
    b=c