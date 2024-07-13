from os import system
system("cls")

def funcs(lst, N):
    if N > len(lst):
        return -1
    
    def func(lst, n):
        if n == 0:
            return max(lst)
        else:
            max_value = max(lst)
            lst.remove(max_value)
            return func(lst, n - 1)
    return func(lst, N)
my_list = [3, 8, 1, 10, 5]
N = int(input("son kiriting : "))
result = funcs(my_list, N)
print(result)