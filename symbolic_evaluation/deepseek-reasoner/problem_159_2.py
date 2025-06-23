import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the simple fraction 16/3 using high-precision arithmetic
numerator = mp.mpf(16)
denominator = mp.mpf(3)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))