s = str(input())
total = len(s)
uc = 0
lc = 0
ws = 0
sym = 0
for i in s:
    if (
        (i >= "!" and i <= "@")
        or (i >= "[" and i <= "^")
        or (i == "`")
        or (i >= "{" and i <= "~")
    ):
        sym += 1
    elif i >= "A" and i <= "Z":
        uc += 1
    elif i >= "a" and i <= "z":
        lc += 1
    elif i == "_":
        ws += 1

print(ws / total)
print(lc / total)
print(uc / total)
print(sym / total)
