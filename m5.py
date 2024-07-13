from collections import Counter
from os import system
system("cls")

def tkror(lst):
    c = Counter(lst)
    m = c.most_common()[-1]
    return m
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 7]
n = tkror(lst)

print(f"{n[0]}  --  {n[1]} marta takrorlangan")