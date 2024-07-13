from os import system
system("cls")

def func(son:list):
    if son > 0:
        return son + 5
    else:
        return son - 5
a = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6]
nat = list(map(func,a))
print(nat)