import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 10
sqrt_10 = mp.sqrt(10)

# Calculate numerator: 2*(sqrt(10) - 3)
numerator = 2 * (sqrt_10 - 3)

# Compute final result by dividing numerator by sqrt(10)
result = numerator / sqrt_10

# Print result with 10 decimal places
print(mp.nstr(result, n=10))