import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate numerator (4 * pi)
numerator = 4 * mp.pi

# Compute final result by dividing numerator by sqrt(3)
result = numerator / sqrt3

# Print result with 10 decimal places
print(mp.nstr(result, n=10))