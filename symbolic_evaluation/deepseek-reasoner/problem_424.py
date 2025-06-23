import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# The analytical solution is exactly zero
result = mp.mpf(0)

# Print result with 10 decimal places of precision
print(mp.nstr(result, n=10))