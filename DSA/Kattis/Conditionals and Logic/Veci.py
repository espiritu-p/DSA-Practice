number = ""
perms = []


def recurse(used, curPerm):
    global number, perms
    if len(curPerm) == len(used):
        perms.append(int(curPerm))
    for i in range(len(used)):
        if not used[i]:
            used[i] = True
            curPerm += number[i]

            recurse(used, curPerm)

            curPerm = curPerm[:-1]
            used[i] = False


def solve():
    global number, perms
    number = input()

    used = [False for _ in number]

    greater_than_input = lambda x: x > int(number)

    curPerm = ""

    recurse(used, curPerm)

    candidates = list(filter(greater_than_input, perms))

    if candidates:
        print(min(candidates))
    else:
        print(0)


def main():
    solve()


if __name__ == "__main__":
    main()
