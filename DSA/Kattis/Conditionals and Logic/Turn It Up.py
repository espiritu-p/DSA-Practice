n = int(input())
volume = 7

for _ in range(n):
    command = input().split()[1][:-1]

    if command == "op" and volume < 10:
        volume += 1
    elif command == "ned" and volume > 0:
        volume -= 1

print(volume)
