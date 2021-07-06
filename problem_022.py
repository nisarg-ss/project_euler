d={chr(i+64):i for i in range(1,27)}
# print(d)
def findsum(s):
    summ=0
    for i in s:
        summ+=d[i]
    return summ

f=open('names.txt','r')
l=(f.read().split(','))
for i in range(len(l)):
    l[i]=l[i][1:-1]
l.sort()

res=0
for i,w in enumerate(l):
    res+=((i+1)*findsum(w))
print(res)


