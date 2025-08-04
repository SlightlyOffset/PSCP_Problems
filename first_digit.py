import math

def get_first_digit(base, exponent):
    log_val = exponent * math.log10(base)
    frac_part = log_val - int(log_val)
    first_digit = int(10 ** frac_part)
    return first_digit

# Example
base = 7
exponent = 40000001
print(f"The first digit of {base}^{exponent} is {get_first_digit(base, exponent)}")
