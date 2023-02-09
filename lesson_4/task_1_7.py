"""
Функция получает на вход словарь с названием компании в
качестве ключа и списком с доходами и расходами (3-10
чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании.
Если все компании прибыльные, верните истину, а если хотя
бы одна убыточная - ложь.
"""


def profit_calculation(data: dict[str, list[int | float]]) -> tuple[dict[str, int | float], bool]:
    result = {}
    is_profit_point = 0
    is_all_profit = set()

    for name, fin_res in data.items():
        spam = sum(fin_res)
        result[name] = spam
        is_all_profit.add(False if spam <= is_profit_point else True)

    return result, all(is_all_profit)


data = {
    'Рога и копыта': [250, 200, -300, 500, -1000, 500],
    'Космос': [1500, 2000, -100, -1000, 2000, 1000],
    'Пыль': [1250, 200, -300, 500, -1000, -2000],
    'ТТТ': [2500, 1200, -500, 1500, -1000, 1000],
}

print(profit_calculation(data))
