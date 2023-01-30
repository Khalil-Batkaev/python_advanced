"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
отрицательных чисел и чисел больше 100 тысяч.
"""

STEP = 2
START = 3
LOW_LIMIT = 1
HIGH_LIMIT = 100_000
IS_PRIME = 'Число яляется простым'
IS_COMPOSITE = 'Число яляется составным'

num = int(input('Введите целое число в диапазоне от 1 до 100 000: '))
if num < LOW_LIMIT or num > HIGH_LIMIT:
    print('Вы ввели число не из заданного диапазона!')
    exit(1)

if num == LOW_LIMIT:
    print(IS_PRIME)
elif not num % STEP:
    print(IS_COMPOSITE)
else:
    for i in range(START, num, STEP):
        if not num % i:
            print(IS_COMPOSITE)
            break
    else:
        print(IS_PRIME)
