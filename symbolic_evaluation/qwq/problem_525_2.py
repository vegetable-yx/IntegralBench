import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the simple fraction 1/2 using high-precision arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(2)
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))