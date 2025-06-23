import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate numerator and denominator using high-precision arithmetic
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Perform the division with extended precision
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))