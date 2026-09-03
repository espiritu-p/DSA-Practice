best_picture = []


def recurse(used, valid_picture, cur_picture):
    global best_picture

    if len(cur_picture) == len(used):
        if not best_picture:
            for student in cur_picture:
                best_picture.append(student)
    for i in range(len(used)):
        if not used[i]:
            if len(cur_picture) > 0 and not valid_picture[cur_picture[-1]][i]:
                continue

            used[i] = True
            cur_picture.append(i)

            recurse(used, valid_picture, cur_picture)

            used[i] = False
            cur_picture.pop()


def solve():
    while True:
        try:
            n = int(input())

            students = [input() for i in range(n)]

            students_dict = {}

            students.sort()

            for i in range(n):
                students_dict[students[i]] = i

            used = [False for _ in range(n)]

            valid_picture = [[True for _ in range(n)] for _ in range(n)]

            num_student_pair = int(input())

            for i in range(num_student_pair):
                s1, s2 = map(str, input().split())
                n1, n2 = students_dict[s1], students_dict[s2]
                valid_picture[n1][n2] = False
                valid_picture[n2][n1] = False

            cur_picture = []

            recurse(used, valid_picture, cur_picture)

            final_class_pic = ""

            global best_picture

            if best_picture:
                for idx in best_picture:
                    for key, value in students_dict.items():
                        if value == idx:
                            final_class_pic += key + " "

                print(final_class_pic.strip())
            else:
                print("You all need therapy.")

            best_picture = []
        except ValueError:
            exit()
        except EOFError:
            exit()


def main():
    solve()


if __name__ == "__main__":
    main()
