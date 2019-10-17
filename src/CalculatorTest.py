import unittest
import Calculator

class KnownValues(unittest.TestCase):
    # Test addition ()
    def test_addition(self):
        results=Calculator.addition(1,2)
        self.assertEqual(3, results)


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
