from os import system
system("cls")

def value(dct:dict):
    mv = max(dct.keys())
    print(f"Max keys qiymat: {mv}")
dct = {'a': 5, 'b': 3, 'c': 4, 'd': 2, 'e': 1}
value(dct)