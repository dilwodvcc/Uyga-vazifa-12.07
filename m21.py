def func(nums):
    if len(nums) < 2:
        print("Ro'yxatda kamida ikkita element bo'lishi kerak.")
        return
    toq = sorted([num for num in nums if num % 2 != 0])[:2]
    print(toq)

lst = e = input("Sonlar kiriting : ").split(' ')
func(lst)