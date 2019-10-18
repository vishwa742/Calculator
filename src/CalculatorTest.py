import unittest
import Calculator
from Calculator import Calc

class KnownValues(unittest.TestCase):
    # Test addition ()
    def test_addition(self):
        results=Calculator.addition(1,2)
        self.assertEqual(3, results)

    def test_instantiate_calculator(self):
        calculator = Calc()
        self.assertIsInstance(calculator, Calc)

    def test_results_property_calculator(self):
        calculator = Calc()
        self.assertEqual(calculator.result, 4)


    #def test_subtraction(self):
        #results=Calculator.subtraction(2,1)
        #self.assertEqual(1, results)

if __name__== '__main__':
    unittest.main()









import unittest
#from Calculator import Calculator
#class MyTestCase(unittest.TestCase):
#
#   def test_instantiate_calculator(self):
#        calculator=Calculator()
#        self.assertIsInstance(calculator, Calculator)

#if __name__ == '__main__':
#    unittest.main()
