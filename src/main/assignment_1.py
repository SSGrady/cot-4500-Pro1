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
# Input: the exact_value taken from double precision
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

if __name__ == "__main__":
    hw_binary = "010000000111111010111001"
    exact_value = double_precision(hw_binary)
    chopped_value = three_digit_chopping(exact_value)
    rounded = three_digit_rounding(exact_value)
    abs_error, rel_error = compute_errors(exact_value, rounded)

    print(f"1) {exact_value:.5f}\n")
    print(f"2) {chopped_value:.5f}\n")
    print(f"3) {rounded:.5f}\n")
    print(f"4a) {abs_error:.5f}\n") 
    print(f"4b) {rel_error:.5f}\n")