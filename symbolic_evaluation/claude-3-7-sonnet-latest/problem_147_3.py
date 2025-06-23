import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the analytical expression: 2π
result = 2 * mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))