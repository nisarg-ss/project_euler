def check(n):
    a=[20,19,18,17,16,15,14,13,12,11]
    for i in a:
        if n%i!=0:
            return False
    return True

ans=21
while(True):
    if check(ans):
        print(ans)
        break
    ans+=1
    