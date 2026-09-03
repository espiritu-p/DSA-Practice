n, w, h = map(int, input().split())

for i in range(n):
    diagonal = (w * w + h * h) ** (0.5)
    match = int(input())
    print("DA" if match <= diagonal else "NE")
