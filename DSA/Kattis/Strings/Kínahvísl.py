word1 = input()
word2 = input()
diff = 1

for i in range(len(word1)):
    if word1[i] != word2[i]:
        diff += 1

print(diff)
