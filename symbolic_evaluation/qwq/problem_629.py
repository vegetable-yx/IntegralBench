import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute numerator and denominator as high-precision floats
numerator = mp.mpf(253)
denominator = mp.mpf(3)

# Calculate the fraction 253/3
fraction = numerator / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))