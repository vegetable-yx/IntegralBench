import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate the simple fraction 3/8 using high-precision arithmetic
numerator = mp.mpf(3)
denominator = mp.mpf(8)
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))