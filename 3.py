def difference(put):
    max_after = 0

    for item in put:
        if len(item[item.find(".") + 1:]) > max_after:
            max_after = len(item[item.find(".") + 1:])

    after = []

    for item in put:
        if item.find(".") != -1:
            after.append(int(item[item.find(".") + 1:].ljust(max_after, "0")))

    result = max(after) - min(after)

    return result


size = int(input("Введите колличество элементов списка: "))
nums = []

print("Введите числа:")

for i in range(size):
    nums.append(input())

print(f"0.{difference(nums)}")



