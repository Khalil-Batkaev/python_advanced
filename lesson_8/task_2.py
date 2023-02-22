import json
import os
from pathlib import Path

__all__ = [
    'json_gen',
]

def json_gen(file: Path):
    result = {}
    unique_id = set()

    if file.is_file() and os.path.getsize(file) > 0:
        with open(file, 'r', encoding='utf-8') as js:
            result = json.load(js)
            unique_id.update(*((value.keys()) for value in result.values()))
    while True:
        name, user_id, lvl = input('Введите данные через пробел: ').split()
        if not user_id in unique_id:
            result.setdefault(int(lvl), {}).update({user_id: name})
            with open(file, 'w', encoding='utf-8') as f:
                print(result)
                if user_id not in unique_id:
                    json.dump(result, f, indent=2)


if __name__ == '__main__':
    json_gen(Path('files', 'names.json'))
