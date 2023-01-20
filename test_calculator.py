import unittest
'''
import program from another file
'''
import calculator

'''
Test Class: Naming can be done as per our requirement
'''


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)
        self .assertEqual(calculator.add(-10, 10), 0)
        self .assertEqual(calculator.add(-10, -10), -20)

    def test_subtract(self):
        result = calculator.subtract(10, 5)
        self.assertEqual(result, 5)
        self .assertEqual(calculator.subtract(-10, 10), -20)
        self .assertEqual(calculator.subtract(-10, -10), 0)

    def test_multiply(self):
        result = calculator.multiply(10, 5)
        self.assertEqual(result, 50)
        self .assertEqual(calculator.multiply(-10, 10), -100)
        self .assertEqual(calculator.multiply(-10, -10), 100)
        self .assertEqual(calculator.multiply(0, -10), 0)

    def test_divide(self):
        result = calculator.divide(10, 5)
        self.assertEqual(result, 2)
        self.assertEqual(calculator.divide(-10, 10), -1)
        self.assertEqual(calculator.divide(-10, -10), 1)
        '''
        For exceptions that will be raised
        '''
        self.assertRaises(ValueError, calculator.divide, 10, 0)
        # Or using context manager we can achieve the same as
        with self.assertRaises(ValueError):
            calculator.divide(20, 0)

    '''
    # This code will not be considered as test case as the naming convention is not followed
    # test_ must preceed every function name to be considered for test case
    def sub_test(self):
        result = calculator.subtract(20,5)
        self.assertEqual(result,15)
    '''


if __name__ == '__main__':
    unittest.main()
