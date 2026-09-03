# get the sequence
seq = str(input())

# initial pos in in the leftmost cup
pos = 1

# update pos per character
for i in seq:
    if i == "A" and pos != 3:
        pos = 2 if (pos == 1) else 1
    elif i == "B" and pos != 1:
        pos = 3 if (pos == 2) else 2
    elif i == "C" and pos != 2:
        pos = 1 if (pos == 3) else 3
    else:
        pass

# display final pos of ball
print(pos)
