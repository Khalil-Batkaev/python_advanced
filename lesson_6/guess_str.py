__all__ = [
    'guess',
    'library',
]


def guess(question: str, answer: list[str], count: int):
    count_ = 0
    print(question)

    while True:
        count_ += 1
        choice = input('Введите отгадку: ').lower()

        if choice in answer:
            return f'Вы угадали с {count_} попытки'
        print(f'Неверно. Осталось {count - count_} попыток')

        if count == count_:
            return f'Вы проиграли'


def library(func, count):
    data = {
        'Без окон, без дверей, полна горница людей': ['огурец', 'арбуз', 'помидор'],
        'И зимой и летом одним цветом': ['елка', 'ель', 'ёлка']
    }
    for key, item in data.items():
        print(func(key, item, count))



if __name__ == '__main__':
    # print(guess('Без окон, без дверей, полна горница людей', ['огурец', 'арбуз', 'помидор'], 5))
    print(library(guess, 3))