import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the simple fraction 1/24 using exact arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(24)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))