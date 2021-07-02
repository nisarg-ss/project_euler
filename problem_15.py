# actually the ans is 20c10

def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans

f20=factorial(40)
f10=factorial(20)
print(f20,f10)
print(f20/(f10*f10))