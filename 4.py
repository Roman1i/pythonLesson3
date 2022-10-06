def bin2(a):
    if a == 3:
        return 11
    if a == 2:
        return 10
    if a % 2 == 0:
        return bin2(int(a // 2)) * 10 + 0
    else:
        return bin2(int(a // 2)) * 10 + 1


print(bin2(int(input("Введите число: "))))
