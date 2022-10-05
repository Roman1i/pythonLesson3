def pare(lst):
    newlist = []
    len2 = 0

    if len(lst) % 2 == 0:
        len2 = int(len(lst) / 2)
    else:
        len2 = int(len(lst) // 2 + 1)

    for i in range(len2):
        newlist.append(lst[i] * lst[-(i + 1)])
    return newlist


size = int(input("Размер списка: "))
nums = []

print("Введите элементы списка:")
for i in range(size):
    nums.append(int(input()))

print(pare(nums))
