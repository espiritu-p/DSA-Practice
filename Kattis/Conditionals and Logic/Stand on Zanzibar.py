n = int(input())

for i in range(n):
    turtles = list(map(int, input().split()))[0:-1]
    lower_bound = 0

    for t in range(1, len(turtles)):
        if turtles[t] > turtles[t - 1] * 2:
            lower_bound += turtles[t] - turtles[t - 1] * 2
    print(lower_bound)
