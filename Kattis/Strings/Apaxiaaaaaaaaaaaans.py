n = str(input())
a = []

for i in range(len(n) - 1):
    if n[i] != n[i + 1]:
        a.append(n[i])
a.append(n[len(n) - 1])
print("".join(a))
