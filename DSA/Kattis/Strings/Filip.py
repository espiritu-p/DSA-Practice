# get two three-digit numbers
x, y = map(str, input().split())

# use the slicing method to reverse each three-digit number
x = x[::-1]
y = y[::-1]

# display the higher reversed number
print(max(int(x), int(y)))
