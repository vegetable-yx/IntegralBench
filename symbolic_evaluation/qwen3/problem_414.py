import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute the analytical result
result = mp.mpf(0)  # Direct assignment of zero value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))