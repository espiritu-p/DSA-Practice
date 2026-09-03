_, _ = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = list(set(a) & set(b))

for elem in a:
    if elem in res:
        print(elem, end=" ")
