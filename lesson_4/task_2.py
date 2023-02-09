"""
Напишите функцию для транспонирования матрицы
"""


def matrix_transposition(matrix: list[list]) -> list[list]:
    new_matrix = []

    for i in range(len(matrix[0])):
        spam = []
        for j in range(len(matrix)):
            spam.append(matrix[j][i])
        new_matrix.append(spam)

    return new_matrix


matrix = [[1, 3, 5], [2, 4, 6], [7, 9, 11], [8, 10, 12]]
print(f'Транспонированная матрица: {matrix_transposition(matrix)}')
