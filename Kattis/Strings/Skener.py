r, c, zr, zc = map(int, input().split())
article = []

for _ in range(r):
    article.append(input())

temp = []
final = []

for i in range(len(article)):
    res = ""
    for scanned in article[i]:
        for j in range(zc):
            res += scanned

    if not res:
        res = article[i]

    temp.append(res)

for e in temp:
    for _ in range(zr):
        final.append(e)

for e in final:
    print(e)
