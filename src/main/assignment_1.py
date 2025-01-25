# src/main/assignment_1.py
import math

# 1. Double Precision Calculation
def double_precision():
    BIAS = 1023
    binary = "010000000111111010111001"

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

print(f"1) {double_precision():.5f}\n") #1) 491.56250
