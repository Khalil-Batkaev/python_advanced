"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
"""

TEXT = """
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as 
dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value 
including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
Elements are counted from an iterable or initialized from another mapping (or counter):
Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising 
a KeyError:
Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising 
a KeyError:
New in version 3.1.
Changed in version 3.7: As a dict subclass, Counter inherited the capability to remember insertion order. Math 
operations on Counter objects also preserve order. Results are ordered according to when an element is first 
encountered in the left operand and then by the order encountered in the right operand.
Counter objects support additional methods beyond those available for all dictionaries:
"""

COUNT = 10

words = TEXT.split()
qty_words = {}

for word in words:
    if word.isalpha():
        _word = word.lower()
        qty_words[_word] = qty_words.setdefault(_word, 0) + 1

result = sorted(qty_words, key=qty_words.get, reverse=True)

print(f'10 самых частых слов: {result[:COUNT]}')
