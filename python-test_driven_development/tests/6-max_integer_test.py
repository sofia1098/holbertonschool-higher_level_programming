#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_empty_list(self):
        """Test empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats_list(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_int_float_list(self):
        """Test list with ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_duplicates(self):
        """Test list with duplicate max values"""
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

if __name__ == '__main__':
    unittest.main()
