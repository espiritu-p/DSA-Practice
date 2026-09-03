n = int(input())

for i in range(n):
    x = input()

    if x.find("Simon says") != -1:
        print(" ".join(x.split(" ")[2:]))
