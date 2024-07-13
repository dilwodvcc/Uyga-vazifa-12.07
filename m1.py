from os import system
system("cls")

def max2(n):
    if len(n) < 2:
        return None 
    
    max1 = float('-inf')
    max2 = float('-inf')

    for a in n:
        if a > max1:
            max2 = max1
            max1 = a
        elif a > max2 and a != max1:
            max2 = a

    return max2
n = [3, 5, 7, 2, 8, 6, 4, 7, 9, 9]
print(max2(n))