import mpmath as mp
mp.dps = 15  # Set internal precision

# Direct assignment of the analytical result
result = mp.mpf(2)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))