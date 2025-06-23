import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute natural logarithm of (1 + sqrt(2))
log_term = mp.log(1 + sqrt2)

# Multiply sqrt2 with the logarithm result
sqrt_log_product = sqrt2 * log_term

# Subtract 1 from the product
numerator = sqrt_log_product - 1

# Multiply by pi/8 to get final result
result = (mp.pi / 8) * numerator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))