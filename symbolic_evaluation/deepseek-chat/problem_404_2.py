import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is exactly zero
result = mp.mpf(0)

# Print the result to exactly 10 decimal places (using 10 significant digits)
print(mp.nstr(result, n=10))