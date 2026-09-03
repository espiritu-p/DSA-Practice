n = int(input())
d = {"keys": 0, "phone": 0, "wallet": 0}

for i in range(n):
    item = input()

    if item in d:
        d[item] += 1

if all(value > 0 for value in d.values()):
    print("ready")
else:
    for key, value in d.items():
        if value == 0:
            print(key)
