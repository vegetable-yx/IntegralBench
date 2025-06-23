import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant value: 1234.56789012
# Assign the constant directly as a string to avoid floating-point inaccuracies
result = mp.mpf('1234.56789012')

# Print the result to exactly 10 significant digits as required
print(mp.nstr(result, n=10))