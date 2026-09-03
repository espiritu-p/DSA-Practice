# get the inputs for the pieces
p = list(map(int, input().split()))

# original list
o = [1, 1, 2, 2, 2, 8]

# subtract input list from the original list
res = list(map(lambda y, x: y - x, o, p))

for i in res:
    print(i, end=" ")
