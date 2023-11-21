import unittest
from calculadora import suma, division

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_division(self):
        with self.assertRaises(ValueError):
            division(10, 0)

if __name__ == '__main__':
    unittest.main()

