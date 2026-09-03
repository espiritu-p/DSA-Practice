import re

n = str(input())
a = re.split("-", n)

for i in a:
    print(i[0], end="")
