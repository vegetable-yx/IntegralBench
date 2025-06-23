import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate the exact fraction 1/4 using high-precision arithmetic
numerator = mp.mpf(1)
denominator = mp.mpf(4)
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))