import unittest

max_integer = __import__('6-max_integer').max_integer

class TestmaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 7, 2, 5, 8]), 8)
    
    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([10, 6, 3, 7]), 10)
    
    def test_empty_string(self):
        self.assertEqual(max_integer(""), None)
    
    def test_floats(self):
        self.assertEqual(max_integer([0.12, 0.87, 1.56, 1.24]), 1.56)
    
    def test_float_integer(self):
        self.assertEqual(max_integer([1, 8.98, 0.34, 4,]), 8.98)
    
    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -3, -5, -8]), -1)

    def test_negative_number(self):
        self.assertEqual(max_integer([-1, 3, 5, 8]), 8)
    
    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()