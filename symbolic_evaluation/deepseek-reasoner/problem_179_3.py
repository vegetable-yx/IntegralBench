import mpmath as mp
mp.dps = 15  # Set internal precision

# The analytical result is exactly to zero
result = mp.mpf(0)

# Print with 10 decimal places precision
print(mp.nstr(result, n=10))