n, q = map(int, input().split())
names = []
queries = []

for _ in range(n):
    names.append(input().split())

for i in range(q):
    queries.append(input())

for query in queries:
    result = ""
    count = 0
    for i in range(len(names)):
        initials = names[i][0][0] + names[i][1][0]

        if query == initials:
            count += 1
            result = " ".join(names[i])

        if i == len(names) - 1:
            if count > 1:
                result = "ambiguous"
            elif count < 1:
                result = "nobody"

    print(result)
