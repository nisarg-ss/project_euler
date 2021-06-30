a,b,c=1,2,3
ans=2
while c<4000000:
    c=a+b
    a=b
    b=c
    if c%2==0:
        ans+=c
print(ans)