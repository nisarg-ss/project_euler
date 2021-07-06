def sum_of_factors(n):
    summ=0
    for i in range(1,n//2+1):
        if n%i==0:
            summ+=i
    return summ

d={}
res=0
for i in range(10000):
    sumfact=sum_of_factors(i)
    d[i]=sumfact
    if d.get(sumfact,0)==i and i!=sumfact:
        print(i,sumfact)
        res+=i
        res+=sumfact
print(res)
