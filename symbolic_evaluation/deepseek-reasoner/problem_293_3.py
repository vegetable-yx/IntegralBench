import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Direct assignment of the analytical result
result = mp.mpf(4)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))