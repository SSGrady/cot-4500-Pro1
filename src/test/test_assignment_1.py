# src/test/test_assignment_1.py
import unittest
import math

from src.main.assignment_1 import (
    approximate_root_two,
    bisection_method,
    fixed_point_iteration,
    newton_raphson_method
)

class TestAssignment1(unittest.TestCase):

    def test_approximate_root_two(self):
        iterations = approximate_root_two(x0=1.5, tol=1e-6)
        self.assertEqual(iterations, 4, f"Expected 4 iterations but got {iterations}.")

    def test_bisection_method(self):
        def f(x):
            return x**3 + 4*x**2 - 10
        p = bisection_method(f, left=1, right=2, tol=1e-3, max_iter=100)
        self.assertGreaterEqual(p, 1.0, "Expected p to be >= 1.0")
        self.assertLessEqual(p, 2.0, "Expected p to be <= 2.0")

    def test_fixed_point_iteration(self):
        def f(x):
            return x**3 + 4*x**2 - 10
        def g_stable(x):
            val = (10 - x**3) / 4.0
            return math.sqrt(val) if val >= 0 else float('nan')
        p = fixed_point_iteration(g_stable, p0=1.5, tol=1e-6, max_iter=50)
        self.assertIsNotNone(p, "Expected p to not be None")
        self.assertAlmostEqual(f(p), 0.0, delta=1e-3)

    def test_newton_raphson_method(self):
        def f(x):
            return math.cos(x) - x
        def f_prime(x):
            return -math.sin(x) - 1
        root = newton_raphson_method(f, f_prime, p0=math.pi/4, tol=1e-10, max_iter=50)
        self.assertAlmostEqual(root, 0.739085, delta=2e-7)

if __name__ == "__main__":
    unittest.main()
