n = int(input())
d = {}

for i in range(n):
    name, fans = map(str, input().split())

    if name not in d:
        d[name] = int(fans)
    else:
        d[name] += int(fans)

print(max(d, key=d.get))
