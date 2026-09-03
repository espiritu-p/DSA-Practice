# get the number of test cases
n = int(input())
for i in range(n):
    x = int(input())
    fac = 1
    #
    for j in range(1, x + 1):
        fac *= j
    print(fac % 10)
