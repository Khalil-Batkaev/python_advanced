__all__ = [
    'Rectangle',
]


class Rectangle:
    """Создает объект Прямоугольник с заданными сторонами"""

    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __str__(self):
        return f'Прямоугольник со сторонами: {self.length}, {self.width}'

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"


if __name__ == '__main__':
    r1 = Rectangle(2)
    r2 = Rectangle(4, 5)
    print(r1)
    print(f'{r2 = }')
