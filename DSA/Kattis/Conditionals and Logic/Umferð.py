m = int(input())
n = int(input())

empty = 0
occupied = 0

for i in range(n):
    cars = str(input().split())
    for car in cars:
        if car == "#":
            occupied += 1
        elif car == ".":
            empty += 1

print(empty / (occupied + empty))
