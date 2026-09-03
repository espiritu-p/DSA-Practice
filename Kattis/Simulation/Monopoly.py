n = int(input())
distance = list(map(int, input().split()))
prob = 0

for x in distance:
    count = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j == x:
                count += 1

    prob += count / 36

print(prob)
