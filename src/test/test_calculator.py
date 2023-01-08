import unittest
import infiniteMath.calculator

class CalculatorTest(unittest.TestCase):

    def __init__(self):
        self.calculator = infiniteMath.calculator.Calculator()

    def add(self):
        self.assertEqual(self.calculator.add("999", "999"), "1998")
        self.assertEqual(self.calculator.add("0", "0"), "0")

    def subtract(self):
        self.assertEqual(self.calculator.subtract("999", "499"), "500")
        self.assertEqual(self.calculator.subtract("999", "1000"), "-1")

    def multiply(self):
        self.assertEqual(self.calculator.add("5", "5"), "25")
        self.assertEqual(self.calculator.add("-5", "5"), "-25")
        self.assertEqual(self.calculator.add("-5", "-5"), "25")
        self.assertEqual(self.calculator.add("2.5", "2.5"), "6.25")

    def divide(self):
        self.assertEqual(self.calculator.add("25", "5"), "5")
        self.assertEqual(self.calculator.add("-25", "5"), "-5")
        self.assertEqual(self.calculator.add("-25", "-5"), "5")
        self.assertEqual(self.calculator.add("12.5", "10"), "1.25")

if __name__ == '__main__':
    unittest.main()