from random import randrange, sample

"""
✔ Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
✔ Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они
не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга. Программа получает на вход
восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если
ферзи не бьют друг друга верните истину, а если бьют — ложь.
✔ Напишите функцию в шахматный модуль. Используйте генератор 
случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных 
расстановки.
"""

__all__ = [
    'eight_queens',
]

_SIZE = 8
_START = 1
_STOP = _SIZE + 1
_LIMIT = 4
_QUEEN = 1
_UP = [1, 2, 3, 4, 5, 6, 7, 8]
_DOWN = [8, 7, 6, 5, 4, 3, 2, 1]


def eight_queens(coords: list[tuple]) -> bool:
    line_coords = set()
    column_coords = set()
    column_coords_list = []

    coords.sort(key=lambda x: x[0])  # Сортировка координат по горизонталям сверху вниз

    for line_coord, column_coord in coords:
        line_coords.add(line_coord)
        column_coords.add(column_coord)
        column_coords_list.append(column_coord)

    # Проверяем, что ферзи стоят на разных горизонталях и вертикалях: 8 различных координат - (проверка на ход ладьи)
    if len(line_coords) != _SIZE or len(column_coords) != _SIZE:
        return False

    # Решение Гаусса: ферзи можно расставить, если сумма заданных отсортированных координат вертикалей со списком чисел
    # от 1 до 8 по возрастанию и убыванию даёт уникальные значения: 8 различных вариантов - (проверка на ход слона)
    column_up_result = {num_1 + num_2 for num_1, num_2 in zip(_UP, column_coords_list)}
    column_down_result = {num_1 + num_2 for num_1, num_2 in zip(_DOWN, column_coords_list)}

    if len(column_up_result) != _SIZE or len(column_down_result) != _SIZE:
        return False

    return True


def coords_gen() -> iter:
    while True:
        # Долгий путь
        # coords = [(randrange(_START, _STOP), randrange(_START, _STOP)) for _ in range(_SIZE)]

        # Быстрый путь: сразу отсекли варианты хода ладьи
        coords = [(line_coord, column_coord) for line_coord, column_coord in zip(sample(_UP, _SIZE), sample(_UP, _SIZE))]
        yield coords


def board_painter(coords: tuple) -> None:
    board = [[0] * _SIZE for _ in range(_SIZE)]

    for line_coord, column_coord in coords:
        board[line_coord - 1][column_coord - 1] = _QUEEN

    print(*board, sep='\n')


if __name__ == '__main__':
    results = set()

    for coords in coords_gen():
        if eight_queens(coords):
            results.add(tuple(coords))
        if len(results) == _LIMIT:
            print(f'Успешные комбинации:', *results, sep='\n')
            break

    for coords in results:
        board_painter(coords)
        print('*' * 50)
