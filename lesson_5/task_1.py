"""
Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило:
“число является простым, если делится нацело только на
единицу и на себя”.
"""


def prime_gen(number: int):
    start = 2
    stop = number + 1

    for num in range(start, stop):
        limit = num // start + 1

        for div in range(start, limit):
            if not num % div:
                break
        else:
            yield num


print(prime_gen(115))
print(*prime_gen(115))
