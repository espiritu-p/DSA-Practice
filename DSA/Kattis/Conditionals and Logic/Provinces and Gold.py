g, s, c = map(int, input().split())
bp = g * 3 + s * 2 + c
if bp >= 2:
    if bp >= 8:
        print("Province", end="")
    elif bp >= 5:
        print("Duchy", end="")
    elif bp >= 2:
        print("Estate", end="")
    print(" or ", end="")
    if bp >= 6:
        print("Gold", end="")
    elif bp >= 3:
        print("Silver", end="")
    elif bp >= 0:
        print("Copper", end="")
else:
    print("Copper")
