n = int(input())
flights = []
ans = []

for _ in range(n):
    flights.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if flights[i][j] != -1:
            ans.append("{} {} {}".format(i + 1, j + 1, flights[i][j]))

print(len(ans))

for answer in ans:
    print(answer)
