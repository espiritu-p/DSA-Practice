n, k, d = map(int, input().split())
num_guests = 0

for i in range(n):
    q_start = int(input())

    if q_start + 14 <= k + d:
        num_guests += 1

print(num_guests)
