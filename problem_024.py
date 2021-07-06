from itertools import permutations

arr=[0,1,2,3,4,5,6,7,8,9]
def permutation():
    perms=list(permutations(arr))
    return ("".join([str(i) for i in perms[999999]]))

print(permutation())    