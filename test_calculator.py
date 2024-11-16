import unittest
from calculator import Calculator 


class TestCalculator(unittest.TestCase):
    def test_add(self): 
      self.assertEqual(Calculator().add(2, 3), 5)
      self.assertEqual(Calculator().add(-2,-3),-5)
      self.assertEqual(Calculator().add(2, -3), -1)

if __name__ == '__main__':
  unittest.main()

