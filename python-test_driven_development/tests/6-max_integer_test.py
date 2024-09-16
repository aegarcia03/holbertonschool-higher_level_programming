import unittest

max_integer = __import__('6-max_integer').max_integer

class TestmaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)
    
    def test_floats(self):
        self.assertEqual(max_integer([0.12, 0.87, 1.56, 1.24]), 1.56)
    
    def test_float_integer(self):
        self.assertEqual(max_integer([1, 8.98, 0.34, 4,]), 8.98)
    
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -5, 8]), 8)

if __name__ == '__main__':
    unittest.main()