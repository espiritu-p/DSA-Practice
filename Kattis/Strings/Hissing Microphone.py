x = str(input())
ctr = 0

for i in range(len(x) - 1):
    if x[i] == "s" and x[i] == x[i + 1]:
        ctr += 1

print("hiss") if (ctr > 0) else print("no hiss")
