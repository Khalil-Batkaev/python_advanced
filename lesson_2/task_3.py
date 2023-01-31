import fractions
import math

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна 
возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.  
"""

numerator_1, denominator_1 = map(int, input('Введите первую дробь: ').split('/'))
numerator_2, denominator_2 = map(int, input('Введите вторую дробь: ').split('/'))
fraction_1 = fractions.Fraction(numerator_1, denominator_1)
fraction_2 = fractions.Fraction(numerator_2, denominator_2)

while True:
    action = input('Введите "сумма", если хотите вычислить сумму или "произведение", если произведение: ').lower()
    if action in ('сумма', 'произведение'):
        break

if action == "сумма":
    print(fraction_1 + fraction_2)
    if denominator_1 == denominator_2:
        new_numerator = numerator_1 + numerator_2
        new_denominator = denominator_1
    else:
        new_denominator = math.lcm(denominator_1, denominator_2)
        new_numerator = numerator_1 * new_denominator / denominator_1 + numerator_2 * new_denominator / denominator_2
else:
    print(fraction_1 * fraction_2)
    new_numerator = numerator_1 * numerator_2
    new_denominator = denominator_1 * denominator_2

divisor = math.gcd(int(new_numerator), new_denominator)
if divisor:
    new_numerator /= divisor
    new_denominator /= divisor

result = f'{int(new_numerator / new_denominator)}' if not new_numerator % new_denominator \
    else f'{int(new_numerator)}/{int(new_denominator)}'

print(f'{action.title()} дробей: {result}')
