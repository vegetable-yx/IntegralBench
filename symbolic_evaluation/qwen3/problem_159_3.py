import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Compute hyperbolic sine of 4
sinh_value = mp.sinh(4)

# Multiply by 2 to get final result
result = 2 * sinh_value

# Print result with 10 decimal places
print(mp.nstr(result, n=10))