import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the simple fraction 2/9 using exact arithmetic
numerator = 2
denominator = 9
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))