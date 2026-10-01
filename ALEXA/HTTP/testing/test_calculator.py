
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        result = self.calc.add(1, 2)
        self.assertEqual(result, 3) #

    def test_add_negative_numbers(self):
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)

    def test_add_zero(self):
        result = self.calc.add(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
