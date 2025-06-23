import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute modified Bessel function of first kind, order 0 at 2
i0_value = mp.besseli(0, 2)

# Calculate the expression (I0(2) - 1)
base_expression = i0_value - 1

# Multiply by 2 for final result
result = 2 * base_expression

# Print with 10 decimal precision
print(mp.nstr(result, n=10))