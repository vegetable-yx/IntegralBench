import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate -3π using mpmath's constant pi
result = -3 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))