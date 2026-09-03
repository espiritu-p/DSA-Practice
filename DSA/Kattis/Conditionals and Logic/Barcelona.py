_, b = map(int, input().split())
bags = list(map(int, input().split()))

if bags[0] == b:
    print("fyrst")
elif bags[1] == b:
    print("naestfyrst")
else:
    print(bags.index(b) + 1, "fyrst", end=" ")
