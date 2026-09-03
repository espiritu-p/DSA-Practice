n = int(input())

for i in range(n):
    c = int(input())
    ctr = 0
    ctr += 1 if (c == 0) else 0
    while c > 0:
        c //= 10
        ctr += 1
    print(ctr)
