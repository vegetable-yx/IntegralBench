import mpmath as mp

# Set internal decimal places to 15 for high precision
mp.dps = 15

# The analytical expression is a constant: 4
result = mp.mpf(4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))