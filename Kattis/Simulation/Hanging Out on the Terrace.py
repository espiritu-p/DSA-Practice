p, e = map(int, input().split())
total = 0
ctr = 0
for i in range(e):
    a, n = map(str, input().split())
    if a == "enter":
        if total + int(n) <= p:
            total += int(n)
        else:
            ctr += 1
    else:
        total -= int(n)
print(ctr)
