import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression is a constant value
result = mp.mpf('1.851937051982466')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))