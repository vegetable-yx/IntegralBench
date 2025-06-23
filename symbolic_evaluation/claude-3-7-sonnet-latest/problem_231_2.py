import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute 2 * pi
result = 2 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))