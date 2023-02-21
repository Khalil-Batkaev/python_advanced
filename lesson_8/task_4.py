import csv
import json
from pathlib import Path


def func(in_file: Path, out_file: Path):
    with open(in_file, 'r', encoding='utf-8') as f, \
            open(out_file, 'a', encoding='utf-8') as out_f:
        csv_reader = csv.reader(f)
        for i, line in enumerate(csv_reader):
            if i >= 1:
                data = {}
                lvl, user_id, name = line
                data['lvl'] = f'{int(lvl):010}'
                data['user_id'] = int(user_id)
                data['name'] = name.title()
                data['hash'] = hash(f'{name}{user_id}')
                json.dump(data, out_f, indent=2)


def csv2json(file_out: Path, file_in: Path) -> None:
    json_list = []
    with open(file_out, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            json_dict = {}
            level, user_id, name = row
            json_dict['level'] = int(level)
            json_dict['id'] = user_id.zfill(10)
            json_dict['name'] = name.title()
            json_dict['hash'] = hash(f'{user_id}{name}')
            json_list.append(json_dict)

    with open(file_in, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, indent=2)


if __name__ == '__main__':
    func(Path('out.csv'), Path('json_from_csv.json'))
