class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=None):
        self._length = length
        self._width = length if width is None else width

    def area(self):
        return self._width * self._length

    def perimeter(self):
        return 2 * (self._width + self._length)

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value: int):
        if value <= 0:
            raise ValueError(f'Длина должна быть > 0')
        self._length = value

    @width.setter
    def width(self, value: int):
        if value <= 0:
            raise ValueError(f'Ширина должна быть > 0')
        self._width = value


if __name__ == '__main__':
    r = Rectangle(1, 2)
    print(r.length)
    