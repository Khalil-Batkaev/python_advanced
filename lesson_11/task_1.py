from time import time

__all__ = [
    'MyStr',
]


class MyStr(str):
    """Добавляет к строке автора и время создания."""

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    def __str__(self):
        # self!r - вызывает repr вместо str
        return f'Строка {self!r} написана автором {self.author}'


if __name__ == '__main__':
    s = MyStr('Hello world!', 'prepod')
    print(s)
    print(s.author)
    s2 = MyStr('Hi', 'student')
    print(s2.author)
    print(s.upper())
    print(s.time, s2.time)
    print(f'{s2 = }')
