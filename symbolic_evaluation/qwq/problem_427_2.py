import mpmath as mp
mp.dps = 15

# Calculate square root of 11
sqrt_11 = mp.sqrt(11)

# Compute numerator: 11 * sqrt(11)
numerator = 11 * sqrt_11

# Compute final result by dividing numerator by 18
result = numerator / 18

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))