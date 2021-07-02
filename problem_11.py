arr=[]
for i in range(20):
    t=[int(j) for j in input().split()]
    arr.append(t)

maxx=0
mul=0
for i in range(20):
    for j in range(17):
        mul=arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3]
        if mul>maxx:
            maxx=mul

for i in range(17):
    for j in range(20):
        mul=arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j]
        if mul>maxx:
            maxx=mul

for i in range(17):
    for j in range(17):
        mul=arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3]
        if mul>maxx:
            maxx=mul

for i in range(17):
    for j in range(19,2,-1):
        mul=arr[i][j]*arr[i+1][j-1]*arr[i+2][j-2]*arr[i+3][j-3]
        if mul>maxx:
            maxx=mul


print(maxx)
