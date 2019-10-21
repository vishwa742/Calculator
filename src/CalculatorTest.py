import unittest, csv
import Calculator
from Calculator import Calc

calculator = Calc()

from var import list


class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calc)

    def test_add_method(self):
        self.assertEqual(calculator.add(2,2), 4)
        #self.assertEqual(calculator.result, 4)

    def test_add_using_csv(self):
        calculator = Calc()
        result_new =0
        for row in list:

            x = row[0]
            y = row[1]
            expect_result = row[2]
            result_new = calculator.add(x,y)

            self.assertEqual(result_new, expect_result)


    def test_subtract_method(self):
        self.assertEqual(calculator.subtract(2,2), 0)  # Using the object add from the class Calc
        #self.assertEqual(calculator.result, 0)



    def test_multiply_method(self):
        self.assertEqual(calculator.multiply(2,3), 6)


    def test_divide_method(self):
        self.assertEqual(calculator.divide(7,5), 1.4)

    def test_square_method(self):
        self.assertEqual(calculator.square(7), 49)

    def test_root_method(self):
        self.assertEqual(calculator.root(49), 7)


    #def test_results_property_calculator(self):
        #self.assertEqual(calculator.result, 4)

if __name__== '__main__':
    unittest.main()

