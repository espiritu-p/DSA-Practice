word = input()
count = 0

for c in word:
    if (c >= "a" and c <= "z") or (c >= "A" and c <= "Z"):
        count += 1

print(count)
