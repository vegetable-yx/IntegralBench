import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Define numerator and denominator
numerator = mp.mpf(1)
denominator = mp.mpf(8)

# Calculate the simple fraction
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))