word = input()
b_count = word.count("b")
k_count = word.count("k")

if b_count == 0 and k_count == 0:
    print("none")
elif b_count > k_count:
    print("boba")
elif b_count < k_count:
    print("kiki")
else:
    print("boki")
