from os import system
system("cls")

def func():
    e = input("Son kiriting : ").split(' ')
    a = list(set(e))
    b = list(map(lambda x:int(x),a))
    print(b)
func()