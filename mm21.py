from os import system
system("cls")

def func():
    a = 1
    c = 0
    while 1:
        if a % 2 != 0:
            print(a)
            c = c + 1
        a = a + 1
        if c == 2:
            break
func()