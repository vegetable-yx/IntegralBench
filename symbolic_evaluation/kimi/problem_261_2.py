import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant value directly
result = mp.mpf('0.4212484375')

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))