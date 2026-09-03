rods = int(input())
length = 0
for i in range(rods):
    length += int(input())

    if i > 0:
        length -= 1

print(length)
