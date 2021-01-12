import unittest
from homework.test_simple_calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)

    def test_subtract(self):
        self.assertEqual(subtract(8, 2), 6)

    def test_multiply(self):
        self.assertEqual(multiply(2, 6), 12)

    def test_divide(self):
        self.assertEqual(divide(20, 10), 2)


if __name__ == '__main__':
    unittest.main()
