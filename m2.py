from os import system
system("cls")

def min2(n):
    if len(n) < 2:
        return None 
    
    min1 = float('inf')
    min2 = float('inf')

    for a in n:
        if a < min1:
            min2 = min1
            min1 = a
        elif a < min2 and a != min1:
            min2 = a

    return min2
n = [3, 5, 7, 2, 8, 6, 4, 7, 9, 9]
print(min2(n))