import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_int_addition(self):
        self.assertEqual(calc.int_addition(10, 5), 15)
        self.assertEqual(calc.int_addition(-1, 1), 0)
        self.assertEqual(calc.int_addition(-1, -1), -2)

    def test_int_subtraction(self):
        self.assertEqual(calc.int_addition(10, 5), 5)
        self.assertEqual(calc.int_addition(-1, 1), -2)
        self.assertEqual(calc.int_addition(-1, -1), 0)

    def test_int_multiply(self):
        self.assertEqual(calc.int_addition(10, 5), 50)
        self.assertEqual(calc.int_addition(-1, 1), -1)
        self.assertEqual(calc.int_addition(-1, -1), 1)

    def test_int_divide(self):
        self.assertEqual(calc.int_addition(10, 5), 2)
        self.assertEqual(calc.int_addition(-1, 1), -1)
        self.assertEqual(calc.int_addition(-1, -1), 1)



if __name__ == '__main__':
    unittest.main()
