import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate numerator and denominator as arbitrary-precision floats
numerator = mp.mpf(80)
denominator = mp.mpf(23)

# Compute the ratio of 80/23 with full precision
ratio = numerator / denominator

# Calculate natural logarithm of the ratio
result = mp.log(ratio)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))