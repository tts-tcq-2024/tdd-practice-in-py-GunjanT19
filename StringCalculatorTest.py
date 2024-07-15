import unittest
from StringCalculator import add  # Assuming add function is implemented in StringCalculator module

class TestStringCalculator(unittest.TestCase):
        
    def test_expectZeroForEmptyInput(self):
        self.assertEqual(add(""), 0)
                
    def test_expectZeroForSingleZero(self):
        self.assertEqual(add("0"), 0)
                
    def test_expectSumForTwoNumbers(self):
        self.assertEqual(add("1,2"), 3)
                
    def test_ignoreNumbersGreaterThan1000(self):
        self.assertEqual(add("1,1001"), 1)
                
    def test_expectSumWithCustomDelimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)
                
    def test_expectSumWithNewlineDelimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_negativeNumbersNotAllowed(self):
        with self.assertRaises(ValueError) as context:
            add("-1,2,-3")
        self.assertEqual(str(context.exception), "negatives not allowed: -1, -3")

    def test_customDelimiterOfAnyLength(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_multipleCustomDelimiters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)

if __name__ == '__main__':
    unittest.main()
