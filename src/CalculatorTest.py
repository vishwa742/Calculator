import unittest, csv
from Calculator import Calc
from csvreader import CsvReader
calculator = Calc()


class KnownValues(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(calculator, Calc)


    def test_add_using_csv(self):
        testData= CsvReader('src/csvaddition.csv').data
        for row in testData:
            x = int(row['Value 1'])
            y = int(row['Value 2'])
            expect_result = int(row['Result'])
            result = calculator.add(x,y)
            self.assertEqual(result, expect_result)



if __name__== '__main__':
    unittest.main()

