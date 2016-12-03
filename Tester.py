import unittest
import Calc

class Tests(unittest.TestCase):
    def test_calc_multiplication(self):
        result = Calc.mult(10,30)
        self.assertEqual(300,result)

if __name__ == '__main__':
    unittest.main()
