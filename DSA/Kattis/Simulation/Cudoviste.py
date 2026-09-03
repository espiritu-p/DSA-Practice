row, col = map(int, input().split())
map = [input() for _ in range(row)]
squash = [0] * 5

for i in range(row - 1):
    for j in range(col - 1):
        park = map[i][j : j + 2] + map[i + 1][j : j + 2]

        if "#" not in park:
            squash[park.count("X")] += 1

print(*(count for count in squash), sep="\n")
