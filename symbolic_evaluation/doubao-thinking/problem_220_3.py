import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by sqrt(2)
sqrt2_pi = sqrt_2 * mp.pi

# Multiply by 5
numerator = 5 * sqrt2_pi

# Divide by 8 to get final result
result = numerator / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))