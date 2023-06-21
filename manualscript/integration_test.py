import calculator
import unittest


class MyTestCase(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculator.multiply(2, 3), 6)

    def test_division(self):
        self.assertEqual(calculator.divide(6, 3), 2)

    def test_divide_by_zero(self):
        try:
            calculator.divide(6, 0)
        except ValueError as e:
            assert str(e) == "Cannot divide by zero"
        else:
            assert False, "Expected ValueError"
