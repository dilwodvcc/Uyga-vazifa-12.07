import os
os.system("cls")

def juft(lst):
    return [elem for elem in lst if elem % 2 == 0]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nat = juft(a)
print(nat)