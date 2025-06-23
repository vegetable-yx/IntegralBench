import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# The analytical expression is the constant π
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))