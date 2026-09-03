word = input()
vowels = ["a", "e", "i", "o", "u", "y"]
count = 0
y_count = 0

for c in word:
    if c in vowels[0:-1]:
        count += 1
    elif c == vowels[-1]:
        y_count += 1

print(count, count + y_count)
s
