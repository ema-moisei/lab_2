"""5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
elements under the main diagonal with 0 (zero)."""


def zero_elements(matrix):
    line_zeros = 1
    max_zeros = len(matrix) - 1
    current_line = 1
    print(max_zeros)
    for line in range(0, max_zeros):
        poz = 0
        for zero in range(0, line_zeros):
            matrix[current_line][poz] = 0
            poz += 1
        current_line += 1
        line_zeros += 1
    print(matrix)


def main():

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    zero_elements(matrix)


if __name__ == "__main__":
    main()
