import unittest

from .matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.m1 = Matrix([[1, 2], [4, 5]])
        self.m2 = Matrix([[1, 2], [4, 5]])
        self.m3 = Matrix([[1, 2, 3], [4, 5, 6]])
        self.m4 = Matrix([[4, 5, 6], [1, 2, 3]])
        self.m5 = Matrix([[2, 2], [4, 5]])

    def test_repr(self):
        self.assertEqual(self.m1, Matrix([[1, 2], [4, 5]]))

    def test_equal(self):
        self.assertEqual(self.m1, self.m2)
        self.assertNotEqual(self.m1, self.m5)
        self.assertNotEqual(self.m1, self.m3)

    def test_add(self):
        self.assertEqual(self.m3 + self.m4, Matrix([[5, 7, 9], [5, 7, 9]]))

    def test_mult(self):
        self.assertEqual(self.m3 * self.m4, Matrix([[6, 9, 12], [21, 30, 39]]))

    def test_size(self):
        self.assertEqual(self.m3._line_size, 2)
        self.assertEqual(self.m3._column_size, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
