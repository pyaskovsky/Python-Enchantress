import unittest
from homework.lib.simple_calc import Calculator


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 5), 7)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(8, 2), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 6), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(20, 10), 2)


if __name__ == '__main__':
    unittest.main()
