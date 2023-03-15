import pytest

from .matrix import Matrix


@pytest.fixture
def get_tuple_matrix() -> tuple:
    m1 = Matrix([[1, 2], [4, 5]])
    m2 = Matrix([[1, 2], [4, 5]])
    m3 = Matrix([[1, 2, 3], [4, 5, 6]])
    m4 = Matrix([[4, 5, 6], [1, 2, 3]])
    m5 = Matrix([[2, 2], [4, 5]])

    return m1, m2, m3, m4, m5


def test_init(get_tuple_matrix):
    assert get_tuple_matrix[0], Matrix([[1, 2], [4, 5]])


def test_equal(get_tuple_matrix):
    assert get_tuple_matrix[0] == get_tuple_matrix[1]
    assert get_tuple_matrix[0] != get_tuple_matrix[2]
    assert get_tuple_matrix[0] != get_tuple_matrix[4]


def test_add(get_tuple_matrix):
    assert get_tuple_matrix[0] + get_tuple_matrix[1] == Matrix([[2, 4], [8, 10]])


def test_mult(get_tuple_matrix):
    assert get_tuple_matrix[2] * get_tuple_matrix[3] == Matrix([[6, 9, 12], [21, 30, 39]])


def test_size(get_tuple_matrix):
    assert get_tuple_matrix[0].get_size() == (2, 2)
    assert get_tuple_matrix[2].get_size() == (2, 3)


if __name__ == '__main__':
    pytest.main(['-v'])
