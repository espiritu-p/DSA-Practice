t = int(input())

for _ in range(t):
    word1 = input()
    word2 = input()
    sim = ""

    for j in range(len(word1)):
        if word1[j] == word2[j]:
            sim += "."
        else:
            sim += "*"

    print(word1, word2, sim, sep="\n")
