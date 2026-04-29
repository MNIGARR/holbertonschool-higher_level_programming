#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Max at the end of an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max somewhere in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max is the first element"""
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_single_element(self):
        """List with one element returns that element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument (default empty list) returns None"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """All negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Mix of positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_duplicate_max(self):
        """List with duplicate max values"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_all_same(self):
        """All elements are identical"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        """Mix of ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_large_numbers(self):
        """Very large integers"""
        self.assertEqual(max_integer([10**9, 10**10, 10**8]), 10**10)

    def test_single_negative(self):
        """Single negative element"""
        self.assertEqual(max_integer([-99]), -99)

    def test_zero_in_list(self):
        """Zero among positive numbers"""
        self.assertEqual(max_integer([0, 1, 2]), 2)

    def test_all_zeros(self):
        """All zeros"""
        self.assertEqual(max_integer([0, 0, 0]), 0)


if __name__ == '__main__':
    unittest.main()
