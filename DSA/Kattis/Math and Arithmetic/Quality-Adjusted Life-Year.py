x = int(input())
a = 0

for i in range(x):
    y, z = map(float, input().split())
    a += y * z

print("{0:.3f}".format(a))
