n, m = map(int, input().split())
word = ""
for i in range(n):
    letters = input()

    for letter in letters:
        if letter >= "a" and letter <= "z":
            word += letter

print(word)
