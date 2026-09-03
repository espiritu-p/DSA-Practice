n = int(input())
ans = 0

for _ in range(n):
    num = input()
    ans += int(num[:-1]) ** int(num[-1])

print(ans)
