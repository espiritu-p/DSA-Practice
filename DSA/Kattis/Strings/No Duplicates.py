x = list(map(str, input().split()))
j = 0
for i in x:
    if x.count(i) > 1:
        print("no")
        break
    else:
        j += 1

if j == len(x):
    print("yes")
