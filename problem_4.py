def ispalindrom(n):
    n_str=str(n)
    if n_str==n_str[::-1]:
        return True
    return False

ans=0
for i in range(100,1000):
    for j in range(100,i+1):
        mul=i*j
        if ispalindrom(mul) and mul>ans:
            ans=mul

print(ans)