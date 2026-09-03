cards = input()
t = 0
c = 0
g = 0

for card in cards:
    if card == "T":
        t += 1
    elif card == "C":
        c += 1
    elif card == "G":
        g += 1

total = t**2 + c**2 + g**2 + 7 * min(t, c, g)

print(total)
