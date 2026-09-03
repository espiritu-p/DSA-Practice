x = int(input())
n = int(input())

total = 0
for i in range(n):
    total += x - int(input())

total += x
print(total)
