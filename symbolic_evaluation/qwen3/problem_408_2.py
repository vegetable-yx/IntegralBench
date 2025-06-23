import mpmath as mp
mp.dps = 15  # Set internal decimal precision to 15 for accurate calculations

# Calculate the fraction 5/3 using high-precision arithmetic
numerator = mp.mpf(5)
denominator = mp.mpf(3)
fraction = numerator / denominator

# Compute natural logarithm of the fraction
log_value = mp.log(fraction)

# Calculate first term (log(5/3)/8)
term1 = log_value / mp.mpf(8)

# Calculate second term (1/20)
term2 = mp.mpf(1) / mp.mpf(20)

# Combine terms for final result
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))