def seq(n):
    c=1
    while(n!=1):
        print
        if n%2!=0:
            n=(3*n)+1
        else:
            n=n>>1
        c+=1
    return c

maxx=0
val=0
for i in range(3,1000000):
    ans=seq(i)
    if ans>maxx:
        maxx=ans
        val=i

print(val)

