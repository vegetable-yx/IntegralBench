import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the simple fraction using exact mpmath operations
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))