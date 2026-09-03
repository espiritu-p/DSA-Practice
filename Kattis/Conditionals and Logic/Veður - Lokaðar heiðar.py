w = int(input())
n = int(input())

for i in range(n):
    road, speed = map(str, input().split())
    print(road, "lokud" if w > int(speed) else "opin")
