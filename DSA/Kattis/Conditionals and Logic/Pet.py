max_score = 0
winner = 0

for i in range(1, 6):
    scores = list(map(int, input().strip().split()))

    if max_score < sum(scores):
        max_score = sum(scores)
        winner = i

print(winner, max_score)
