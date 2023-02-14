from random import randint
import sys

__all__ = [
    'guess_num',
]


def guess_num(start: int, end: int, qty_try: int) -> bool:
    result = randint(start, end)
    count = 0

    while True:
        count += 1
        var = int(input('Введите число: '))

        if var == result:
            return True
        if var < result:
            print(f'Загаданное число больше')
        else:
            print(f'Загаданное число меньше')

        if count == qty_try:
            return False


if __name__ == '__main__':
    print(guess_num(*(int(elem) for elem in sys.argv[1:])))

