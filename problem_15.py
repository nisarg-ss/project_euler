# actually the ans is 20c10

def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans

f20=factorial(20)
f10=factorial(10)
print(f20,f10)
print(f20/(f10*f10))