import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the simple fraction using exact precision
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))