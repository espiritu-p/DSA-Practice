def get_measurement(yarn):
    if yarn == ".":
        return 20
    elif yarn == "O":
        return 10
    elif yarn == "\\":
        return 25
    elif yarn == "/":
        return 25
    elif yarn == "A":
        return 35
    elif yarn == "^":
        return 5
    elif yarn == "v":
        return 22


n, _ = map(int, input().split())
total = 0

for i in range(n):
    garment = input()

    for material in garment:
        total += get_measurement(material)

print(total)
