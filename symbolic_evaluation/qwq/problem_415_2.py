import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate simple fraction using exact values
numerator = mp.mpf(4)
denominator = mp.mpf(5)
result = numerator / denominator

# Output result with exactly 10 decimal places
print(mp.nstr(result, n=10))