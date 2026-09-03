n = int(input())

for i in range(n):
    # gets the beats and seconds
    b, p = map(float, input().split())
    # displays the minimum ABPM, BPM, and maximum ABPM respectively
    print((60 * b / p) - (60 / p), 60 * b / p, (60 * b / p) + (60 / p), end=" ")
