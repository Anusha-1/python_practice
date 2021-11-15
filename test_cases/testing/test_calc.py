import unittest

import calc

class TestCalc(unittest.TestCase): #test suite
    def test_add(self):  # function should always start with test_
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)

        with self.assertRaises(ValueError):
            calc.divide(10,0)
            
if __name__ =='__main__':
    unittest.main()
    #print("Ran one test")