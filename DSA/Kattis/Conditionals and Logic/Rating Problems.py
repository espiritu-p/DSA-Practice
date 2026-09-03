n, k = map(int, input().split())
rating = 0

for _ in range(k):
    judge_rtg = int(input())
    rating += judge_rtg

print((rating + (-3) * (n - k)) / n, (rating + 3 * (n - k)) / n)
