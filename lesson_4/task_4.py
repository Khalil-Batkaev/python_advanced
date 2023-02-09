import decimal

"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
операции - функции. Дополнительно сохраняйте все операции поступления и
снятия средств в список.
"""

ONE = 1
BASE = 50
EXIT = 'выйти'
INSERT = 'пополнить'
WITHDRAW = 'снять'
INSERT_OPERATIONS = 'получить список операций пополнения'
WITHDRAW_OPERATIONS = 'получить список операций снятия'
COMMISSION = decimal.Decimal(1.5 / 100)
MIN_COMMISSION = 30
MAX_COMMISSION = 600
QTY_OPERATION = 3
DEPOSIT_RATE = decimal.Decimal(3 / 100)
TAX_RATE = decimal.Decimal(10 / 100)
MAX_AMOUNT = 5_000_000


def check_action(action: str, amount: decimal.Decimal, insert_operations: list, withdraw_operations: list) -> bool:
    if action not in (INSERT, EXIT, WITHDRAW, INSERT_OPERATIONS, WITHDRAW_OPERATIONS):
        print(f'Вы ввели неверную операцию...\nОстаток на счёте {round(amount, 2)}')
        return False
    if action == EXIT:
        print(f'Остаток на счёте {round(amount, 2)}.\nДо свидания!')
        exit(0)
    if action == INSERT_OPERATIONS:
        print(get_insert_operations(insert_operations))
        return False
    if action == WITHDRAW_OPERATIONS:
        print(get_withdraw_operations(withdraw_operations))
        return False
    return True


def check_amount(amount: decimal.Decimal, new_amount: decimal.Decimal, action: str) -> bool:
    if new_amount and new_amount % BASE:
        print(f'Вы ввели неверную сумму...\nОстаток на счёте {round(amount, 2)}')
        return False
    if action == WITHDRAW and new_amount > amount:
        print(f'Запрошенная сумма больше остатка!\nОстаток на счёте {round(amount, 2)}')
        return False
    return True


def tax_calculation(amount: decimal.Decimal) -> decimal.Decimal:
    amount *= (ONE - TAX_RATE)
    print(f'Списан налог.\nОстаток на счёте {round(amount, 2)}')
    return amount


def commission_calculation(amount: decimal.Decimal) -> float:
    fee = round(amount * COMMISSION, 2)
    fee = max(MIN_COMMISSION, min(fee, MAX_COMMISSION))
    return fee


def deposit_calculation(amount: decimal.Decimal) -> decimal.Decimal:
    amount *= (ONE + DEPOSIT_RATE)
    print(f'Начислены проценты!\nОстаток на счёте {round(amount, 2)}')
    return amount


def insert(amount: decimal.Decimal, new_amount: decimal.Decimal, operations: list) -> decimal.Decimal:
    amount += new_amount
    operations.append((new_amount, amount))
    print(f'Счет пополнен. Остаток на счёте {round(amount, 2)}')
    return amount


def withdraw(amount: decimal.Decimal, new_amount: decimal.Decimal, operations: list) -> decimal.Decimal:
    amount -= new_amount
    fee = commission_calculation(new_amount)
    operations.append((new_amount, amount, fee))
    print(f'Выдача {round(_amount - fee, 2)}\nОстаток на счёте {round(amount, 2)}')
    return amount


def get_insert_operations(opearations: list) -> str:
    return f'Список операций пополнения: {opearations}'


def get_withdraw_operations(opearations: list) -> str:
    return f'Список операций снятия: {opearations}'


amount = decimal.Decimal(0)
count = 0
insert_operations = []
withdraw_operations = []

print('Добро пожаловать!')
while True:
    action = input(f'Выберите операцию из следующих '
                   f'{INSERT}, {WITHDRAW}, {EXIT}, {INSERT_OPERATIONS}, {WITHDRAW_OPERATIONS}: ').lower()

    if amount > MAX_AMOUNT:
        amount = tax_calculation(amount)
    if not check_action(action, amount, insert_operations, withdraw_operations):
        continue

    _amount = decimal.Decimal(input(f'Введите суммy, кратную {BASE}: '))

    if not check_amount(amount, _amount, action):
        continue

    if action == INSERT:
        amount = insert(amount, _amount, insert_operations)
    else:
        amount = withdraw(amount, _amount, withdraw_operations)

    count += 1
    if not count % QTY_OPERATION:
        amount = deposit_calculation(amount)
