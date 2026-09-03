import re

n = int(input())
ctr = 0
for i in range(n):
    btn = str(input())
    if re.search("pink", btn, re.IGNORECASE) or re.search("rose", btn, re.IGNORECASE):
        ctr += 1

print(ctr) if (ctr > 0) else print("I must watch Star Wars with my daughter")
