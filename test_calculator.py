import Calculator
import unittest
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.x =34
        self.y =30
    def tearDown(self):
        self.x = 0
        self.y = 0

    def test_add(self):
        x = 10
        y = 20
        result = Calculator.add(self.x, self.y)
        self.assertEqual(result, self.x+self.y)

    def test_sub(self):
        x = 20
        y = 10
        result = Calculator.sub(self.x, self.y)
        self.assertEqual(result, self.x-self.y)
    def test_mul(self):
        x = 10
        y = 20
        result = Calculator.mul(self.x,self.y)
        self.assertEqual(result, self.x*self.y)
    def test_div(self):
        x = 100
        y = 20
        result = Calculator.div(self.x,self.y)
        self.assertEqual(result, self.x/self.y)


if __name__=="__main__":
    unittest.main()