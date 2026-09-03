n = int(input())
best = ["", 0]


for _ in range(n):
    name, score = map(str, input().split())

    if int(score) > best[1]:
        best[0], best[1] = name, int(score)


print(best[0])
