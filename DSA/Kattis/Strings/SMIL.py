seq = input()
smiles = [":)", ";)", ":-)", ";-)"]
ans = []

for smile in smiles:
    loc = seq.find(smile)
    while seq.find(smile) != -1:
        ans.append(seq.find(smile))
        seq = seq.replace(smile, "x" * len(smile), 1)

ans.sort()

print("\n".join(str(answer) for answer in ans))
