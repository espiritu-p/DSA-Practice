n = int(input())
price = 0

if n > 2020:
    add = n - 2020
    price = 1000 + 100 * add
else:
    price = 1000

print(price)
