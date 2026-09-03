n = int(input())
knots = list(map(int, input().split()))
learned = list(map(int, input().split()))

print(list(set(knots) - set(learned))[0])
