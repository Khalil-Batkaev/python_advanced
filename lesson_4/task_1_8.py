"""
Создайте несколько переменных заканчивающихся и не
оканчивающихся на “s”.
Напишите функцию, которая при запуске заменяет
содержимое переменных оканчивающихся на s (кроме
переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые
переменные без s на конце.
"""


def change_s_atr():
    spam = globals().copy()
    len_limit = 1

    for key, item in spam.items():
        if len(key) > len_limit and key.endswith('s'):
            globals()[key[:-1]], globals()[key] = item, None


s = 2
ts = 20
ess = 155
edfs = 1101
test_1s = 'test'
ok = 1
num = 30
frd = 'tr'

print(globals())
change_s_atr()
print(globals())
