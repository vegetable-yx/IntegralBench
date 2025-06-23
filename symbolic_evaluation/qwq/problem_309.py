import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Divide square root of 2 by 2
sqrt_2_over_2 = sqrt_2 / 2

# Multiply by pi to get final result
result = sqrt_2_over_2 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))