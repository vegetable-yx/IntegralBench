import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate the simple fraction using exact arithmetic
numerator = mp.mpf(128)
denominator = mp.mpf(153)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))