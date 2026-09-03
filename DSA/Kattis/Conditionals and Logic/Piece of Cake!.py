n, h, v = map(int, input().split())
x = []

x.append(h * v * 4)
x.append((n - h) * v * 4)
x.append(h * (n - v) * 4)
x.append((n - h) * (n - v) * 4)

print(max(x))
