import mpmath as mp

# Set the decimal precision for internal calculations
mp.dps = 15

# Compute the constant 2 * pi
result = 2 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))