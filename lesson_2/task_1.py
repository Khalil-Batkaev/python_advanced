import decimal

"""
Задание №6
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
Любое действие выводит сумму денег
"""

ONE = 1
BASE = 50
EXIT = 'выйти'
INSERT = 'пополнить'
WITHDRAW = 'снять'
COMMISSION = decimal.Decimal(1.5 / 100)
MIN_COMMISSION = 30
MAX_COMMISSION = 600
QTY_OPERATION = 3
DEPOSIT_RATE = decimal.Decimal(3 / 100)
TAX_RATE = decimal.Decimal(10 / 100)
MAX_AMOUNT = 5_000_000

amount = decimal.Decimal(0)
count = 0

print('Добро пожаловать!')
while True:
    action = input(f'Выберите операцию из следующих {INSERT}, {WITHDRAW}, {EXIT}: ').lower()

    if amount > MAX_AMOUNT:
        amount *= (ONE - TAX_RATE)
        print(f'Списан налог.\nОстаток на счёте {round(amount, 2)}')

    if action not in (INSERT, EXIT, WITHDRAW):
        print(f'Вы ввели неверную операцию...\nОстаток на счёте {round(amount, 2)}')
        continue
    elif action == EXIT:
        print(f'Остаток на счёте {round(amount, 2)}.\nДо свидания!')
        break
    else:
        _amount = decimal.Decimal(input(f'Введите суммy, кратную {BASE}: '))
        if _amount % BASE:
            print(f'Вы ввели неверную сумму...\nОстаток на счёте {round(amount, 2)}')
            continue

        if action == INSERT:
            amount += _amount
            print(f'Счет пополнен. Остаток на счёте {round(amount, 2)}')
        else:
            if _amount > amount:
                print(f'Запрошенная сумма больше остатка!\nОстаток на счёте {round(amount, 2)}')
                continue

            amount -= _amount
            fee = round(_amount * COMMISSION, 2)

            if fee < MIN_COMMISSION:
                fee = MIN_COMMISSION
            elif fee > MAX_COMMISSION:
                fee = MAX_COMMISSION

            print(f'Выдача {round(_amount - fee, 2)}\nОстаток на счёте {round(amount, 2)}')

        count += 1
        if not count % QTY_OPERATION:
            amount *= (ONE + DEPOSIT_RATE)
            print(f'Начислены проценты!\nОстаток на счёте {round(amount, 2)}')
