import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Define numerator and denominator
numerator = mp.mpf(5)
denominator = mp.mpf(6)

# Calculate the simple fraction
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))