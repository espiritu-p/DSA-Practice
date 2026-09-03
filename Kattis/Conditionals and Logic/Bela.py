# get hand and suit
n, s = map(str, input().split())
total = 0

# add corresponding value (dominant/non-dominant) to total
for i in range(int(n) * 4):
    d = str(input())
    if d[0] == "A":
        total += 11
    elif d[0] == "K":
        total += 4
    elif d[0] == "Q":
        total += 3
    elif d[0] == "T":
        total += 10
    elif d[0] == "J":
        if d[1] == s:
            total += 20
        else:
            total += 2
    elif d[0] == str(9):
        if d[1] == s:
            total += 14
        else:
            pass
    else:
        pass

# display the total points
print(total)
