#https://github.com/CrunchyFire/Lab-11-MZ-BT
#Partner 1: Michael Zhang
#Partner 2: Benjamin Thanapaisarnkij

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(22,mul(11,2))
        self.assertEqual(-22, mul(-11, 2))
        self.assertEqual(22, mul(-11, -2))

    def test_divide(self): # 3 assertions
        self.assertEqual(15, mul(3, 45))
        self.assertRaises(ZeroDivisionError, mul(0, 2))
        self.assertEqual(-2, mul(-3, 6))

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(4,hypotenuse(3,4))
        self.assertRaises(ValueError,hypotenuse,-3,4)
        self.assertRaises(ValueError,hypotenuse,-3,-4)
    #     fill in code

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(4, square_root(16))
        self.assertEqual(5, square_root(25))
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()