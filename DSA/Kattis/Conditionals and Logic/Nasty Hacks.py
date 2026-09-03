n = int(input())

for i in range(n):
    x, y, z = map(int, input().split())
    r = x - (y - z)
    (
        print("advertise")
        if (r < 0)
        else print("do not advertise") if (r > 0) else print("does not matter")
    )
