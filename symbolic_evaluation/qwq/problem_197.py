import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the simple fraction 1/4 using exact mpmath operations
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))