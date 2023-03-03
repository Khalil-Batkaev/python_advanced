class Archive:
    """При первом запуске создает экземпляр класса, при повторном - добавляет в архив прежние данные."""
    instance = None
    count_archive = []
    text_archive = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            # cls.instance.count_archive = []
            # cls.instance.text_archive = []
        else:
            cls.instance.count_archive.append(cls.instance.count)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text

    def __str__(self):
        return f'Архив содержит следующий текст: {self.text_archive} и числа {self.count_archive}'

    def __repr__(self):
        return f"Archive({self.count}, '{self.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    d2 = Archive(2, 'b')
    print(d2.text, d2.text_archive)
    d3 = Archive(3, 'c')
    print(d3.text, d3.text_archive)
    print(d3)
    print(f'{d3 = }')

