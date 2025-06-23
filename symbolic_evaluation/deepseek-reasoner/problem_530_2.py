import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm
log_argument = 3 + 2 * sqrt2

# Calculate natural logarithm of the argument
log_term = mp.log(log_argument)

# Multiply sqrt2 with the logarithmic term
sqrt2_log_product = sqrt2 * log_term

# Final calculation: 3 minus the product
result = 3 - sqrt2_log_product

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))