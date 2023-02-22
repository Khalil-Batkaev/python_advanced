import csv
import json
import pickle
from pathlib import Path

__all__ = [
    'read_csv_to_pickle',
]

"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Распечатайте его как pickle строку.
"""


def read_csv_to_pickle(file: Path) -> bytes:
    data = {}

    with open(file, 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)

        for i, line in enumerate(csv_reader):
            if i == 0:
                for key in line:
                    data[key] = {}
            else:
                for key, value in zip(data, line):
                    spam = value.replace("'", '"')
                    eggs = json.loads(spam)

                    data[key].update(eggs)
    return pickle.dumps(data)


if __name__ == '__main__':
    print(read_csv_to_pickle(Path('files', 'names.csv')))
