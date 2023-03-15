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
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        """
        self.matrix = matrix
        self._line_size = len(self.matrix)
        self._column_size = len(self.matrix[0])

    def __eq__(self, other):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6]]) == Matrix([[1, 2, 3], [4, 5, 6]])
        True
        >>> Matrix([[1, 2, 3], [4, 5, 6]]) == Matrix([[4, 5, 6], [1, 2, 3]])
        False
        """
        for i in range(self._line_size):
            for j in range(self._column_size):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __add__(self, other):
        """
        >>> print(Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[4, 5, 6], [1, 2, 3]]))
            5     7     9
            5     7     9
        >>> Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[4, 5, 6], [1, 2, 3]])
        Matrix([[5, 7, 9], [5, 7, 9]])
        >>> Matrix([[1, 2], [4, 5]]) + Matrix([[4, 5], [1, 2]])
        Matrix([[5, 7], [5, 7]])
        """
        new_matrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self._column_size)]
                      for i in range(self._line_size)]
        return Matrix(new_matrix)

    def __mul__(self, other):
        """
        >>> print(Matrix([[1, 2], [4, 5]]) * Matrix([[4, 5], [1, 2]]))
            6     9
           21    30
        >>> Matrix([[1, 2], [4, 5]]) * Matrix([[4, 5], [1, 2]])
        Matrix([[6, 9], [21, 30]])
        >>> Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[4, 5, 6], [1, 2, 3]])
        Matrix([[6, 9, 12], [21, 30, 39]])
        """
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
        """
        >>> print(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
            1     2     3
            4     5     6
            7     8     9
        """
        result = [' '.join(f'{num:>{self._shift}}' for num in line) for line in self.matrix]
        return '\n'.join(result)

    def __repr__(self):
        """
        >>> Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        """
        return f'Matrix({self.matrix})'


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
