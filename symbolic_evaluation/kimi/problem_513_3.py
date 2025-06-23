import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate the simple fraction using exact mpmath operations
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))