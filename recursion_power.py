def power_recursive(base, exponent):
    """
    Raises a number to the power of exponent using recursion,
    without 'pow', '**', 'for', or 'while'.
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        # Handle negative exponents: x^-n = 1 / x^n
        return 1 / power_recursive(base, -exponent)
    elif exponent % 2 == 0:
        # If exponent is even: x^n = (x^(n/2))^2
        half_power = power_recursive(base, exponent // 2)
        return half_power * half_power
    else:
        # If exponent is odd: x^n = x * x^(n-1)
        return base * power_recursive(base, exponent - 1)

# Example usage:
print(power_recursive(2, 3))   # Output: 8
print(power_recursive(5, 0))   # Output: 1
print(power_recursive(2, -2))  # Output: 0.25
print(power_recursive(3, 4))   # Output: 81
print(power_recursive(7, 1))   # Output: 7
