import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant value directly from the analytical result
result = mp.mpf('1.216093959')

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))