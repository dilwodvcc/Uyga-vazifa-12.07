from os import system
system("cls")

def value(dct:dict):
    mv = max(dct.values())
    print(f"Max valuse qiymat: {mv}")
dct = {'a': 5, 'b': 3, 'c': 4, 'd': 2, 'e': 1}
value(dct)