"""
✔ Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
✔ Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они
не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга. Программа получает на вход
восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если
ферзи не бьют друг друга верните истину, а если бьют — ложь.
"""

_SIZE = 8
_UP = [1, 2, 3, 4, 5, 6, 7, 8]
_DOWN = [8, 7, 6, 5, 4, 3, 2, 1]


def eight_queens(coords: list[tuple]) -> bool:
    line_coords = set()
    column_coords = set()
    column_coords_list = []

    for first_coord, second_coord in coords:
        line_coords.add(first_coord)
        column_coords.add(second_coord)
        column_coords_list.append(second_coord)

    if len(line_coords) != _SIZE or len(column_coords) != _SIZE:
        return False

    up_result = {num_1 + num_2 for num_1, num_2 in zip(_UP, column_coords_list)}
    down_result = {num_1 + num_2 for num_1, num_2 in zip(_DOWN, column_coords_list)}

    if len(up_result) != _SIZE or len(down_result) != _SIZE:
        return False

    return True


if __name__ == '__main__':
    print(eight_queens([(1, 3), (2, 7), (3, 2), (4, 8), (5, 5), (6, 1), (7, 4), (8, 6)]))
