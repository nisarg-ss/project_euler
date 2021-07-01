import math

def isprime(n):
    for i in range(3,(n//2)+1):
        if n%i==0:
            return False
    return True

count=2
prime=3
i=5
while(count!=10001):
    if isprime(i)==True:
        count+=1
        prime=i
        # print(prime,count)
    i+=2
print(prime,count)


