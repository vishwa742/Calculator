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
            self.assertEqual(calculator.add(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))


    def test_sub_using_csv(self):
        test_file= CsvReader('src/subtraction.csv').data
        for row in test_file:
            self.assertEqual(calculator.subtract(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))


    def test_multiply_using_csv(self):
        test_file= CsvReader('src/multiplication.csv').data
        for row in test_file:
            self.assertEqual(calculator.multiply(int(row['Value 1']),int(row['Value 2'])), int(row['Result']))
if __name__== '__main__':
    unittest.main()

