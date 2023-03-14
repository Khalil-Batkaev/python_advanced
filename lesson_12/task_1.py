import json
from collections import deque
from pathlib import Path


class Factorial:
    def __init__(self, k: int):
        self.memory = deque(maxlen=k)

    def __call__(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        self.memory.append({n: result})
        return result

    def view(self):
        return self.memory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.json_file = Path('task.json').open('w', encoding='utf-8')
        json.dump([*self.memory], self.json_file)
        self.json_file.close()


if __name__ == '__main__':
    with Factorial(3) as f:
        print(f(5))
        print(f(2))
        print(f(12))
        print(f(7))
        print(f(21))
        print(f.view())
