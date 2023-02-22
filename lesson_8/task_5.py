import json
import pickle
from pathlib import Path

__all__ = [
    'search_json',
]

"""
Напишите функцию, которая ищет json файлы в указанной
директории и сохраняет их содержимое в виде
одноимённых pickle файлов.
"""


def search_json(directory: Path):
    for file in directory.glob('*.json'):
        with (
            open(file, 'r', encoding='utf-8') as json_f,
            open(Path(directory, file.stem + '.pickle'), 'wb') as pickle_f
        ):
            json_data = json.load(json_f)
            pickle.dump(json_data, pickle_f)


if __name__ == '__main__':
    search_json(Path('files'))
