from os import system
system("cls")

def key(d):
    if not isinstance(d, dict):
        raise ValueError("Funksiyaga faqat dictionary kiritishingiz kerak.")
    
    max_value = max(d.values())
    for key, value in d.items():
        if value == max_value:
            return key

dct = {'a': 10, 'b': 5, 'c': 15, 'd': 7}
nat = key(dct)
print(nat)