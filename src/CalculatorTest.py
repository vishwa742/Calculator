import unittest
import Calculator
from Calculator import Calc

calculator = Calc()

class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calc)

    def test_add_method(self):
        self.assertEqual(calculator.add(2,2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method(self):
        self.assertEqual(calculator.subtract(2,2), 0)  # Using the object add from the class Calc
        self.assertEqual(calculator.result, 0)

    def test_results_property_calculator(self):
        self.assertEqual(calculator.result, 4)


if __name__== '__main__':
    unittest.main()

