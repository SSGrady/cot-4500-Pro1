# src/test/test_assignment_1.py
import unittest
from src.main.assignment_1 import *

class TestAssignment1(unittest.TestCase):
    def setUp(self):
        # Precompute values used across tests below
        self.binary = "010000000111111010111001"
        self.exact_value = double_precision(self.binary)
        self.chopped_value = three_digit_chopping(self.exact_value)
        self.rounded_value = three_digit_rounding(self.exact_value)
        self.abs_error, self.rel_error = compute_errors(self.exact_value, self.rounded_value)
    
    def test_double_precision(self):
        self.assertAlmostEqual(self.exact_value, 491.56250, places=5)
    
    def test_three_digit_chopping(self):
        self.assertEqual(self.chopped_value, 491.00000)
    
    def test_three_digit_rounding(self):
        self.assertEqual(self.rounded_value, 492.00000)
    
    def test_absolute_error(self):
        self.assertAlmostEqual(self.abs_error, 0.43750, places=5)
    
    def test_relative_error(self):
        self.assertAlmostEqual(self.rel_error, 0.00089, places=5)
    
    def test_minimum_terms(self):
        self.assertEqual(minimum_terms(), 21)
    
    def test_bisection_iterations(self):
        self.assertEqual(bisection_iterations(), 16)
    
    def test_newton_raphson_iterations(self):
        self.assertEqual(newton_raphson_iterations(), 6)

if __name__ == "__main__":
    unittest.main()