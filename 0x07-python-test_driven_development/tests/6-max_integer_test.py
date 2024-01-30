#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    def test_max_integer_with_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_integer_with_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_max_integer_with_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, 3, -4, 2]), 3)

if __name__ == '__main__':
    unittest.main()
