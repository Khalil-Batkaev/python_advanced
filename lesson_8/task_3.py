import csv
import json
import os
from pathlib import Path

__all__ = [
    'get_from_user',
]

def get_from_user(file: Path) -> None:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)

    rows = []
    for level, value in json_file.items():
        for user_id, name in value.items():
            rows.append({'level': level, 'user_id': user_id, 'name': name})

    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        print(json_file)
        fieldnames = ['level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    get_from_user(Path('files/names.json'))
