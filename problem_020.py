def fact(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans

summ=fact(100)
ans=0
for i in str(summ):
    ans+=int(i)
print(ans)