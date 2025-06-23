import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by 3 and pi
result = -3 * sqrt2 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))