w = int(input())
n = int(input())
area = 0

for i in range(n):
    wi, li = map(int, input().split())
    area += wi * li

print(area // w)
