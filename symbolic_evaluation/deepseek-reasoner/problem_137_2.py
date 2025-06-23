import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Direct assignment of the analytical result
result = mp.mpf(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))