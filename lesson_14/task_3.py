from string import ascii_letters

"""
Напишите для задачи 1 тесты pytest. Проверьте
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
import pytest


def text_filter(s: str) -> str:
    result = ''.join(c for c in s if c in set(ascii_letters + ' '))
    return result.lower()


def test_no_change():
    assert text_filter('hello world') == 'hello world'


def test_lower_case():
    assert text_filter('Hello World') == 'hello world'


def test_marks():
    assert text_filter('hello, world') == 'hello world'


def test_no_ascii():
    assert text_filter('hello Питонистический world') == 'hello  world'


def test_global():
    assert text_filter('Hello123, Питонистический World!') == 'hello  world'


if __name__ == '__main__':
    pytest.main(['-v'])
