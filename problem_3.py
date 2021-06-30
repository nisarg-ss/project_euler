import math

n=600851475143
arr=set()

for i in range(2,int(math.sqrt(n))+1):
    while n%i==0:
        arr.add(i)
        n=n/i

if len(arr)==0:
    arr.add(n)

print(*sorted(list(arr)))