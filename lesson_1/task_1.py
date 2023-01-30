"""
Задание №8
Нарисовать в консоли ёлку спросив у пользователя количество
рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********
"""

START = 1
STEP = 2

qty = int(input('Сколько рядов у ёлки? '))
stop = qty * STEP

for i in range(START, stop, STEP):
    print(('*' * i).center(stop-START))

print()

"""
Задание №9
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на
школьной тетрадке.
"""

START = 2
MIDDLE = 6
STOP = 11
TEN = 10

for i in range(START, STOP):
    for j in range(START, MIDDLE):
        print(f'{j} * {i} = {j * i}', end='\t')
        if j == STOP // START:
            print()
print()
for i in range(START, STOP):
    for j in range(MIDDLE, TEN):
        print(f'{j} * {i} = {j * i}', end='\t')
        if j == STOP - START:
            print()
