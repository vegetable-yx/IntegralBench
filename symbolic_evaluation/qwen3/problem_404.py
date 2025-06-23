import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical result
result = mp.mpf(0)

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))