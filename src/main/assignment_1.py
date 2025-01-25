# src/main/assignment_1.py
import math

# 1. Double Precision Calculation
# Input: binary a truncated 64-bit string in IEEE 754 format

def double_precision(binary):
    BIAS = 1023

    sign = int(binary[0])
    exponent_bits = binary[1:12]
    # pading with zeros
    mantissa_bits = binary[12:] + '0' * (52 - len(binary[12:]))

    # calculate exponent using: int(val, base)
    exponent = int(exponent_bits, 2) - BIAS

    # calculate matissa
    mantissa = 1.0
    for i in range(len(mantissa_bits)):
        mantissa += int(mantissa_bits[i]) * 2 ** (-i - 1)
    value = (-1) ** sign * (2 ** exponent) * mantissa

    return value



# 2. Three-Digit Chopping
def three_digit_chopping(value):
    if value == 0:
        return 0.0000
    magnitude = math.floor(math.log10(abs(value)))
    scale_factor = 10 ** (3 - 1 - magnitude)
    scaled_value = value * scale_factor
    chopped = int(scaled_value) / scale_factor
    return float(f"{chopped:.5f}")

# 3. Three-Digit Rounding
def three_digit_rounding(value):
    if value == 0:
        return 0.00000
    magnitude = math.floor(math.log10(abs(value)))
    scale = 10 ** (3 - 1 - magnitude)
    scaled_value = value * scale
    rounded = round(scaled_value) / scale
    return float(f"{rounded:.5f}")

# 4. Absolute & Relative Error
def compute_errors(exact, approx):
    absolute = abs(exact - approx)
    relative = absolute / abs(exact)
    return (absolute, relative)

# 5. Minimum Terms for the Series Convergence
def minimum_terms():
    tol = 1e-4
    n = 1
    while True:
        if 1 / ((n+1) ** 3) < tol:
            return n
        n += 1

# 6a. Bisection Method Iterations
def bisection_iterations():
    f = lambda x: x ** 3 + 4 * x ** 2 - 10
    a, b = -4.0, 7.0
    tol = 1e-4
    iterations = 0

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return iterations

# 6b. Newton-Raphson
def newton_raphson_iterations():
    f = lambda x: x ** 3 + 4 * x ** 2 - 10
    f_prime = lambda x: 3 * x ** 2 + 8 * x
    x_0 = 7.0
    tol = 1e-4
    iterations = 0

    while True:
        x_1 = x_0 - f(x_0) / f_prime(x_0)
        if abs(x_1 - x_0) < tol:
            break
        x_0 = x_1
        iterations += 1
    return iterations

def fixed_point_iteration(g, x_0, tol=1e-4, max_iter=100):
    iterations = 0
    while iterations < max_iter:
        x_1 = g(x_0)
        if abs(x_1 - x_0) < tol:
            break
        x_0 = x_1
        iterations += 1
    return iterations

if __name__ == "__main__":
    hw_binary = "010000000111111010111001"
    exact_value = double_precision(hw_binary)
    chopped_value = three_digit_chopping(exact_value)
    rounded = three_digit_rounding(exact_value)
    abs_error, rel_error = compute_errors(exact_value, rounded)
    terms = minimum_terms()
    bisect_iterations = bisection_iterations()
    newton_iterations = newton_raphson_iterations()

    print(f"1) {exact_value:.5f}\n")
    print(f"2) {chopped_value:.5f}\n")
    print(f"3) {rounded:.5f}\n")
    print(f"4a) {abs_error:.5f}\n") 
    print(f"4b) {rel_error:.5f}\n")
    print(f"5) {terms}\n")
    print(f"6a) {bisect_iterations}\n")
    print(f"6b) {newton_iterations}")