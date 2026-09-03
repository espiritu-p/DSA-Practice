n = int(input())
ans = []

for _ in range(n):
    ans.append(input())

for _ in range(n):
    print(ans.pop(-1))
