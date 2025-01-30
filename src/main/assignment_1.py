# src/main/assignment_1.py
import math

# Approximation algorithm (2.1 - slide 11)
def approximate_root_two(x0: float, tol: float):
    print("===============================")
    print("|approximation algorithm (2.1)|")
    print("===============================\n")
    iteration = 0
    diff = x0
    x = x0

    print(f"{iteration} : {x}")
    while diff >= tol:
        iteration += 1
        old_x = x
        x = (x / 2) + (1 / x)  # Newton iteration for sqrt(2)
        print(f"{iteration} : {x}")
        diff = abs(x - old_x)

    print(f"\nConvergence after {iteration} iterations\n")
    return iteration

# Bisection algorithm (2.1 - slide 14)
def bisection_method(f, left, right, tol=1e-3, max_iter=50):
    print("\n==========================")
    print("|bisection (2.1) algorithm|")
    print("==========================\n")
    i = 0
    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2.0
        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p
    p = (left + right) / 2.0
    print(f"Bisection approximate root = {p:.6f} after {i} iterations\n")
    return p

# Fixed Point Iteration (2.2 - slide 13)
def fixed_point_iteration(g, p0, tol=1e-4, max_iter=50):
    print("\n==========================")
    print("| fixed-point (2.2) method|")
    print("==========================\n")
    i = 1
    result = "Failure"
    while i <= max_iter:
        p = g(p0)
        if math.isinf(p) or math.isnan(p):
            print("\nResult Diverges")
            break
        print(f"{i} : {p:.6f}")
        if abs(p - p0) < tol:
            result = "Success"
            return p
        i += 1
        p0 = p
    print(f"\n{result} after {i} iterations\n")

def newton_raphson_method(f, f_prime, p0, tol=1e-6, max_iter=50):
    print("\n=================================")
    print("| newton-raphson (2.3) algorithm|")
    print("=================================\n")
    i = 1
    result = "Failure"
    while i <= max_iter:
        denom = f_prime(p0)
        if denom == 0:
            print(f"\nDerivative zero at iteration {i}. Unsuccessful.")
            break
        p = p0 - f(p0) / denom
        if math.isinf(p) or math.isnan(p):
            print(f"\nResult diverges at iteration {i}")
            break
        print(f"{i} : {p:.10f}")
        if abs(p - p0) < tol:
            result = "Success"
            print(f"\n{result} after {i} iterations\n")
            return p
        p0 = p
        i += 1
    print(f"\n{result} after {i-1} iterations")
    return p0

if __name__ == "__main__":
   # Ch 2.1: slide 17 example
    def bisection_f(x):
        return x**3 + 4*x**2 - 10
    # Ch 2.2: slides 14 and 15
    def g_example(x):
        return x - (x*x*x) - (4*x*x) + 10  
    # Solve f(x) = cos(x) - x = 0 on [0, π/2], Ch 2.3: slide 8
    def newton_raphson_f(x):
        return math.cos(x) - x
    # Ch 2.3: slide 8
    def newton_raphson_f_prime(x):
        return -math.sin(x) - 1

    # Ch 2.1: slide 11
    approximate_root_two(x0=1.5, tol=1e-6)

    
    bisection_method(bisection_f, left=1, right=2, tol=1e-3)
    fixed_point_iteration(g=g_example, p0=1.5, tol=1e-6, max_iter=50)
    newton_raphson_method(newton_raphson_f, newton_raphson_f_prime, p0=math.pi/4, tol=25*1e-17, max_iter=50)