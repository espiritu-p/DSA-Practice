n = int(input())
count = 0

for i in range(n):
    seq = input()

    if seq.find("CD") == -1:
        count += 1

print(count)
