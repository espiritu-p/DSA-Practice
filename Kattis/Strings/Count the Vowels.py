word = input()
count = 0
vowels = ["a", "e", "i", "o", "u"]

for c in word:
  if c.lower() in vowels:
    count+=1

print(count)