range_nums = input().split(";")
total = 0

for nums in range_nums:
    num = nums.split("-")

    if len(num) > 1:
        total += int(num[1]) - int(num[0]) + 1
    else:
        total += 1

print(total)
