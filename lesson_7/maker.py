from pathlib import Path
from random import choices, randint
from string import ascii_letters, digits

__all__ = [
    'maker_files'
]


"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением. 
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""


def make_files(directory: Path, extension: str, min_name: int = 6, max_name: int = 30,
               min_size: int = 256, max_size: int = 4096, count: int = 42):
    symbols = ascii_letters+digits

    for _ in range(count):
        name = ''.join(choices(symbols, k=randint(min_name, max_name)))
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        file_path = Path(directory, f'{name}.{extension}')

        if not file_path.exists():
            with open(file_path, 'wb') as f:
                f.write(data)


"""
✔ Доработаем предыдущую задачу. 
✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
✔ Расширения и количество файлов функция принимает в качестве параметров. 
✔ Количество переданных расширений может быть любым. 
✔ Количество файлов для каждого расширения различно. 
✔ Внутри используйте вызов функции из прошлой задачи.

✔ Дорабатываем функции из предыдущих задач. 
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции. 
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции 
(добавьте проверки). 
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""


def maker_files(extensions: dict, directory: Path = Path().cwd()):
    directory.mkdir(parents=True, exist_ok=True)

    for extension, count in extensions.items():
        make_files(directory=directory, extension=extension, count=count)


if __name__ == '__main__':
    file_extensions = {
        'mpeg': 2,
        'avi': 3,
        'jpeg': 5,
        'mp4': 2,
        'gif': 1,
        'png': 4,
    }

    maker_files(file_extensions, Path('files'))
    maker_files(file_extensions)
