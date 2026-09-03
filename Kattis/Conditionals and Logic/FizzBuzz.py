# get the inputs
x, y, z = map(int, input().split())

for i in range(1, z + 1):
    # if i is not divisible by both x and y, print i
    if i % x != 0 and i % y != 0:
        print(i)
    # if i is divisible by both x and y, print FizzBuzz
    elif i % x == 0 and i % y == 0:
        print("FizzBuzz")
    # if i is only divisible by x, print Fizz
    elif i % x == 0:
        print("Fizz")
    # if i is only divisible by y, print Buzz
    elif i % y == 0:
        print("Buzz")
