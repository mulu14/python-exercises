import unittest
from source.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_one_operator_sum_value_level_1(self):
        """
        Test strings sum  
        """
        data = "10 + 20"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 30)

    def test_one_operator_subtraction_level_1(self):
        """
        Test strings subtraction
        """
        data = "10 - 20"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, -10)

    def test_one_operator_multiplication_level_1(self):
        """
        Test strings multiplication
        """
        data = "10 * 20"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 200)

    def test_one_operator_division_level_1(self):
        """
        Test two strings divisions
        """
        data = "1 / 3"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 0.333333333333333333)

    def test_multiple_operators_sum_level_2(self):
        """
        Test multiple operators sum level 2
        """
        data = "2+30+4"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 36)

    def test_multiple_operators_subtraction_level_2(self):
        """
        Test multiple operators subtraction level 2
        """
        data = "2 - 3 + 4 + 15"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 18)

    def test_multiple_operators_multiplication_level_2(self):
        """
        Test multiple operators multiplication level 2
        """
        data = "2*3*4"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 24)

    def test_multiple_operators_division_level_2(self):
        """
        Test multiple operators division level 2
        """
        data = "2*3/4 * 20"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 30)

    def test_multiple_operators_sum_level_3(self):
        """
        Test multiple operators sum level 3
        """
        data = "2+3*40"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 122)

    def test_multiple_operators_subtraction_level_3(self):
        """
        Test multiple operators subtraction level 3
        """
        data = "2*3 + 4"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, 10)

    def test_multiple_operators_multiplication_level_3(self):
        """
        Test multiple operators multiplication level 3
        """
        data = "2 - 3*4"
        result = Calculator.calculate(self, data)
        self.assertEqual(result, -10)

    def test_multiple_operators_division_level_3(self):
        """
        Test multiple operators division level 3
        """
        data = "2/3 + 4 - 1"
        result = Calculator.calculate(self, data)
        self.assertEqual(result,  3.666666666666667)


if __name__ == '__main__':
    unittest.main()
