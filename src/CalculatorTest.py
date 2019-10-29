import unittest, csv
from Calculator import Calc
from csvreader import CsvReader
calculator = Calc()


class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calc)


    def test_add_using_csv(self):
        test_file= CsvReader('src/csvaddition.csv').data
        for row in test_file:
            x = int(row['Value 1'])
            y = int(row['Value 2'])
            expect_result = int(row['Result'])
            result_final = calculator.add(x,y)
            self.assertEqual(result_final, expect_result)


    def test_sub_using_csv(self):
        test_file= CsvReader('src/subtraction.csv').data
        for row in test_file:
            x = int(row['Value 1'])
            y = int(row['Value 2'])
            expect_result = int(row['Result'])
            result_final = calculator.subtract(x,y)
            self.assertEqual(result_final, expect_result)


if __name__== '__main__':
    unittest.main()

