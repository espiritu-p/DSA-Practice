while True:
    n = int(input())

    if n == -1:
        break

    prev_elapsed = 0
    total = 0
    for i in range(n):
        speed, elapsed = map(int, input().split())
        total += speed * (elapsed - prev_elapsed)
        prev_elapsed = elapsed
    print("{} miles".format(total))
