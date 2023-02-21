import csv
import pickle
from pathlib import Path

"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 (вероятно, задание 5 имеется в виду) этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""

# Если честно, то не до конца понял задание...решение как есть))


def from_pickle_to_csv(file: Path):
    with (
        open(file, 'rb') as pickle_f,
        open(Path(file.parent, file.stem + '.csv'), 'w', encoding='utf-8', newline='') as csv_f
    ):
        data = pickle.load(pickle_f)
        csv_writer = csv.writer(csv_f)

        headers = [key for key in data]
        csv_writer.writerow(headers)
        data = [value for value in data.values()]
        csv_writer.writerow(data)


if __name__ == '__main__':
    from_pickle_to_csv(Path('files', 'names.pickle'))
