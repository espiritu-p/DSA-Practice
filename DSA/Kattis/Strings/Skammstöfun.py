_ = input()
sentence = input()

words = sentence.split(" ")

for word in words:
    if "A" <= word[0] <= "Z":
        print(word[0], end="")
