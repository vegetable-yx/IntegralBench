import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the analytical result
result = mp.mpf(0)  # Direct assignment of zero value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))