import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the analytical expression: -6 * π
result = -6 * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))