import unittest
#Тут импортнуть calculate как допишут


class TestCalculator(unittest.TestCase):

    def test_add(self):
      self.assertEqual(calculator.add(4,7), 11)

    def test_subtract(self):
      self.assertEqual(calculator.subtract(10,5), 5)

    def test_multiply(self):
      self.assertEqual(calculator.multiply(3,7), 21)

    def test_divide(self):
      self.assertEqual(calculator.divide(10,2), 5)


if __name__ == "__main__":
  unittest.main()