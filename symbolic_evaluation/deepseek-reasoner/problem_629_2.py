import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the fraction 253/3 using high-precision arithmetic
numerator = mp.mpf(253)
denominator = mp.mpf(3)
fraction = numerator / denominator

# Compute natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))