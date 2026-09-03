# get x and y coordinate
x = int(input())
y = int(input())

# print which quadrant the coordinate-pair falls into
(
    print(1)
    if (x > 0 and y > 0)
    else print(2) if (x < 0 and y > 0) else print(3) if (x < 0 and y < 0) else print(4)
)
