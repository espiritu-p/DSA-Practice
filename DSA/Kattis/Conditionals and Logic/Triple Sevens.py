n = int(input())
flag = False

for i in range(3):
    wheel = list(map(int, input().split()))

    if 7 not in wheel:
        print(0)
        break
    elif i == 2:
        print(777)
