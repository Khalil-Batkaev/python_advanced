"""
Уникальные данные
"""

# int_list = [10, 2, 3, 1, 4, 1, 2, 6]
#
# list_from_set = list(set(int_list))
# print(f'{list_from_set = }')
#
# list_from_cycle = []
# for num in int_list:
#     if num not in list_from_cycle:
#         list_from_cycle.append(num)
# print(f"{list_from_cycle = }")

"""
Проверка введённый данных
"""

# data = input('Введите что-то: ')
# if data.isdigit() and int(data) >= 0:
#     print('Целое положительное число')
# elif data.isalpha():
#     if data.lower() == data:
#         print('В нижнем регистре')
#     else:
#         print('Верхний регистр')
# elif data.count('-') <= 1 and data[1:].count('-') == 0 and data.count('.') == 1 \
#      and data.replace('-', '').replace('.', '').isdigit():
#     print('Вещественное')

"""
Словарь со списком типов
"""

# random_tuple = (1, 2.13, 5, 8.12, 'hello', 8, 'hi', True, [1, 2, 3], [4, 5, 6])
# result_dict = {}
#
# for item in random_tuple:
#     item_type = type(item)
#     if item_type in result_dict:
#         result_dict[item_type] += [item]
#     else:
#         result_dict[item_type] = [item]
#
# print(result_dict)
#
# d = {}
#
# for i in random_tuple:
#     d.setdefault(type(i), []).append(i)
# print(d)

"""
Удалить элементы равные count
"""

# COUNT = 2
# list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
# spam = {}
#
# for num in list_num:
#     if num in spam:
#         spam[num] += 1
#     else:
#         spam[num] = 1
#
# for key, item in spam.items():
#     if item == COUNT:
#         for _ in range(COUNT):
#             list_num.remove(key)
#
# print(list_num)

"""
Создать список индексов нечётных элементов
"""
# TWO = 2
#
# list_num = [1, 2, 1, 3, 2, 1, 4, 5, 4, 5, 6, 5]
# result = []
#
# for i, num in enumerate(list_num, start=1):
#     if num % TWO:
#         result.append(i)
#
# print(result)

"""
Вывести слова из строки по алфавиту с индексом
"""
# START_NUM = 1
#
# data = input('Введите текст: ').split()
# data.sort()
# max_len = 0
#
# for item in data:
#     if len(item) > max_len:
#         max_len = len(item)
#
# for i, item in enumerate(data, start=START_NUM):
#     print(f'{i} {item:>{max_len}}')

"""
Подсчитать количество букв в тексте
"""

# text = 'sf gdsg fdgfd sgwehshfshshsfd sdg hdhdfhd dsgsg'
# res = {}
# for c in text:
#     res[c] = res.setdefault(c, 0) + 1
# print(res)
#
# text = 'sf gdsg fd$gfd sgwehsh2532fshsh#sfd sdg hdhdfhd dsgsg121241323#'
# res = {}
# for c in set(text):
#     res[c] = text.count(c)
# print(res)


"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
какие вещи взяли все три друга
какие вещи уникальны, есть только у одного друга
какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции
"""
