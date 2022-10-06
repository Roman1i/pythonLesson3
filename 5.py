def fibonacci_number(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci_number(a - 1) + fibonacci_number(a - 2)

def negafibonacci_list(a):
    lst = []
    for i in range(a):
        if (a - i) % 2 == 0:
            lst.append(-fibonacci_number(a - i))
        else:
            lst.append(fibonacci_number(a - i))
    lst.append(0)
    for i in range(a):
        lst.append(fibonacci_number(i + 1))
    return lst

print(negafibonacci_list(int(input("k= "))))
