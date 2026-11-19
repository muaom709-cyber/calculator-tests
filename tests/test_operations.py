import unittest
from calculator_pkg.operations import calculate


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2, "+", 3), 5)

    def test_subtract(self):
        self.assertEqual(calculate(10, "-", 4), 6)

    def test_multiply(self):
        self.assertEqual(calculate(3, "*", 5), 15)

    def test_divide(self):
        self.assertEqual(calculate(20, "/", 4), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10, "/", 0)


if __name__ == "__main__":
    unittest.main()
