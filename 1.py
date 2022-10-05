nums = [2, 6, 8, 9, 4, 3]
result = 0

for i in range(len(nums)):
    if i % 2 == 1:
        result += nums[i]

print(result)
