import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator as high-precision floats
numerator = mp.mpf(253)
denominator = mp.mpf(3)

# Compute the fraction 253/3 with full precision
fraction = numerator / denominator

# Calculate the natural logarithm of the fraction
result = mp.log(fraction)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))