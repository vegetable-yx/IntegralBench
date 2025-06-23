import mpmath as mp
mp.dps = 15  # Set decimal precision for all calculations

# The analytical solution is a simple integer value
result = mp.mpf(9)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))