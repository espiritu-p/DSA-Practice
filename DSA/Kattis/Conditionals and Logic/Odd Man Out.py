n = int(input())

for i in range(n):
    g = int(input())
    codes = list(map(int, input().split()))
    lone = [code for code in codes if codes.count(code) == 1]
    print("Case #{}: {}".format(i + 1, lone[0]))
