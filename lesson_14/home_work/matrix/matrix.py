from random import randint

__all__ = [
    'Matrix',
]

"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать, 
○ сравнения, 
○ сложения, 
○ *умножения матриц
"""

_MIN = 0
_MAX = 100
_line_size = 3


class Matrix:
    """Создает объект Матрица из заданного списка"""
    _shift = 5

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self._line_size = len(self.matrix)
        self._column_size = len(self.matrix[0])

    def __eq__(self, other):
        if self._line_size != other.get_size()[0] or self._column_size != other.get_size()[1]:
            return False

        for i in range(self._line_size):
            for j in range(self._column_size):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        new_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self._column_size)]
                      for i in range(self._line_size)]
        return Matrix(new_matrix)

    def __mul__(self, other):
        result = []
        for i in range(self._line_size):
            spam = []
            for j in range(self._column_size):
                eggs = []
                for k in range(self._line_size):
                    eggs.append(self.matrix[i][k] * other.matrix[k][j])
                spam.append(sum(eggs))
            result.append(spam)
        return Matrix(result)

    def __str__(self):
        result = [' '.join(f'{num:>{self._shift}}' for num in line) for line in self.matrix]
        return '\n'.join(result)

    def __repr__(self):
        return f'Matrix({self.matrix})'

    def get_size(self):
        return self._line_size, self._column_size
