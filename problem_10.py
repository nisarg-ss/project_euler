def isprime(n):
    for i in range(3,(n//2)+1):
        if n%i==0:
            return False
    return True

summ=5
i=5

while(i<2000000):
    if isprime(i):
        summ+=i
        print(i)
    i+=2

print(summ)