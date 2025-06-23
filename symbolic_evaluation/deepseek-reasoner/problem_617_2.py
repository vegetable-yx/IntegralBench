import mpmath as mp
mp.dps = 15  # Set internal precision

# Direct assignment of the analytical result
result = mp.mpf(0)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))