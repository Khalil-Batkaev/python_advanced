"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию
hex используйте для проверки своего результата.
"""

BASE = 16
DATA = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

while True:
    number = int(input('Введите целое число: '))
    if number >= 0:
        break

_number = number
result = ''

while _number:
    _num = _number % BASE
    result = DATA[_num] + result
    _number //= BASE

print(f'Шестнадцатеричное строковое представление числа {number} - {result}')
print(hex(number))
