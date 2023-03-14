from string import ascii_letters
import unittest

"""
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери
символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""


from string import ascii_letters


def text_filter(s: str) -> str:
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()


class TestTextFilter(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(text_filter('hello world'), 'hello world')

    def test_lower_case(self):
        self.assertEqual(text_filter('Hello World'), 'hello world')

    def test_marks(self):
        self.assertEqual(text_filter('hello, world'), 'hello world')

    def test_no_ascii(self):
        self.assertEqual(text_filter('hello Питонистический world'), 'hello  world')

    def test_global(self):
        self.assertEqual(text_filter('Hello123, Питонистический World!'), 'hello  world')


if __name__ == '__main__':
    unittest.main(verbosity=2)
    