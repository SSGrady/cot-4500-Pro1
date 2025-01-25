# src/main/assignment_1.py
import math

# 1. Double Precision Calculation
# Input: binary a truncated 64-bit string in IEEE 754 format
hw_binary = "010000000111111010111001"
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
    value = (-1) ** sign *(2 ** exponent) * mantissa

    return value

exact_value = double_precision(hw_binary)



# 2. Three-Digit Chopping
def three_digit_chopping(value):
    if value == 0:
        return 0.0000
    magnitude = math.floor(math.log10(abs(value)))
    scale_factor = 10 ** (3 - 1 - magnitude)
    scaled_value = value * scale_factor
    chopped = int(scaled_value) / scale_factor
    return float(f"{chopped:.5f}")


chopped_value = three_digit_chopping(exact_value)

def print_hw1():
    print(f"1) {exact_value:.5f}\n") #1) 491.56250
    print(f"2) {chopped_value:.5f}\n") #2) 491.00000

print_hw1()