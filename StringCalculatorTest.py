import unittest
from StringCalculator import add
class TestStringCalculator(unittest.TestCase):
        
        def test_expectZeroForEmptyInput(self): #Testcase1.
                self.assertEqual(add(""), 0)
                
        def test_expectZeroForSingleZero(self): #Testcase2.
                self.assertEqual(add("0"), 0)
                
        def test_expectSumForTwoNumberst(self): #Testcase3.
                self.assertEqual(add("1,2"), 3)
                
        def test_ignoreNumbersGreaterThan1000(self): #Testcase4.
                self.assertEqual(add("1,1001"), 1)
                
        def test_expectSumWithCustomDelimiter(self): #Testcase5.
                self.assertEqual(add("//;\n1;2"), 3)
                
        def test_expectSumWithNewlineDelimiter(self): #Testcase6.
                self.assertEqual(add("1\n2,3"),6);
        




if __name__ == '__main__':
    unittest.main()
