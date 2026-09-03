def get_matrix_size(n):
    row = 1
    temp = n
    col = n

    while row < col:
        row += 1

        if temp % row == 0:
            col = temp // row

    return row, col


def encrypt_message(row, col, message):
    matrix = [["" for _ in range(col)] for _ in range(row)]
    letter_idx = 0

    for i in range(row):
        for j in range(col):
            matrix[i][j] = message[letter_idx]
            letter_idx += 1

    for i in range(col):
        for j in range(row):
            print(matrix[j][i], end="")


def main():
    message = input()

    row, col = get_matrix_size(len(message))

    encrypt_message(row, col, message)


if __name__ == "__main__":
    main()
