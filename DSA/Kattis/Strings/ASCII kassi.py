n = int(input())

if n == 0:
    print("++\n++")

else:
    for i in range(n + 2):
        if i == 0 or i == n + 1:
            print("+" + "-" * n + "+")
        else:
            print("|" + " " * n + "|")
