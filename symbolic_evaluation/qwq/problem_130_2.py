import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate hyperbolic sine of 1
sinh_1 = mp.sinh(1)

# Combine components for final result
result = 2 * sqrt_2 * sinh_1

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))