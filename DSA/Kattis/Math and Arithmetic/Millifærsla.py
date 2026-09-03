a = int(input())
b = int(input())
c = int(input())

cost_dict = {"Monnei": a, "Fjee": b, "Dolladollabilljoll": c}

print(min(cost_dict, key=cost_dict.get))