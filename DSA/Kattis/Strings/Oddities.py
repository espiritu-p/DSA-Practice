x = int(input())

for i in range(x):
    n = int(input())
    print(str(n) + " is odd") if (n % 2 != 0) else print(str(n) + " is even")
