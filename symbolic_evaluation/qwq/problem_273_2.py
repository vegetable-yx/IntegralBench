import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the numerical approximation directly
result = mp.mpf('0.0999')

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))