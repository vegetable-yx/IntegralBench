import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Direct assignment of the analytical result
result = mp.mpf(1)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))