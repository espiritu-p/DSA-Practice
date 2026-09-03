word = input()
days = 0

for i in range(len(word)):
    if (
        (i + 1) % 3 == 1
        and word[i] != "P"
        or (i + 1) % 3 == 2
        and word[i] != "E"
        or (i + 1) % 3 == 0
        and word[i] != "R"
    ):
        days += 1

print(days)
