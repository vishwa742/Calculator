import unittest, csv
import Calculator
from Calculator import Calc

calculator = Calc()

list = ([580, 459, 1039],
        [799, 187, 986],
        [986, 921, 1907],
        [49, 359, 408],
        [508, 114, 622],
        [209, 585, 794],
        [711, 828, 1539],
        [865, 736, 1601],
        [769, 226, 995],
        [559, 870, 1429],
        [838, 494, 1332],
        [521, 927, 1448],
        [844, 738, 1582],
        [987, 977, 1964],
        [91, 143, 234],
        [585, 46, 631],
        [933, 233, 1166],
        [355, 489, 844])

class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calc)

    def test_add_method(self):
        self.assertEqual(calculator.add(2,2), 4)
        self.assertEqual(calculator.result, 4)

    def test_add_using_csv(self):
        calculator = Calc()
        for row in list:

            x = row[0]
            y = row[1]
            expect_result = row[2]
            result_new = calculator.add(x,y)

            self.assertEqual(result_new, expect_result)


    def test_subtract_method(self):
        self.assertEqual(calculator.subtract(2,2), 0)  # Using the object add from the class Calc
        self.assertEqual(calculator.result, 0)

    def test_results_property_calculator(self):
        self.assertEqual(calculator.result, 4)


if __name__== '__main__':
    unittest.main()

