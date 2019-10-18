import unittest
import Calculator
from Calculator import Calc

calculator = Calc()

class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        #calculator = Calc()
        self.assertIsInstance(calculator, Calc)

    def test_addition(self):
        #calculator = Calc()
        results=Calculator.addition(1,2)   # Calling the function from Calculator.py
        self.assertEqual(3, results)
        self.assertEqual(calculator.add(2,2), 4)  # Using the object add from the class Calc




    #def test_subtraction(self):
        #results=Calculator.subtraction(2,1)
        #self.assertEqual(1, results)

    def test_results_property_calculator(self):
        calculator = Calc()
        self.assertEqual(calculator.result, 0)


if __name__== '__main__':
    unittest.main()



    #def test_add_method_calculator(self):
        #calculator = Calc()
        #self.assertEqual(calculator.add(2,2), 4)





