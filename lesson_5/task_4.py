"""Создайте функцию генератор чисел Фибоначчи (см. Википедию) """


def fibonacci_gen(qty: int) -> iter:
    first, second = 0, 1

    for num in range(qty + 1):
        yield first
        first, second = second, first + second


check = '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711'
print(fibonacci_gen(22))
print(*fibonacci_gen(22))
