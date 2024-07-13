from os import system
system("cls")

def func():
    e = input("Son kiriting : ").split(' ')
    a = list(set(e))
    print(a)
func()