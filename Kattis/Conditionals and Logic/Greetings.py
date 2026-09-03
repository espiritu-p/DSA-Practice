# get the input "hey"
x = str(input())

# get the middle of the word "hey"
e = x[1 : len(x) - 1]

# put 'e' for each 'e' in the input
for i in range(len(e)):
    e += "e"

# display the result
print("h" + e + "y")
