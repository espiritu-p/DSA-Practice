word = input()
encoding = input()

for i in range(0, len(encoding), 3):
    print(word[int(encoding[i : i + 3]) - 1], end="")
