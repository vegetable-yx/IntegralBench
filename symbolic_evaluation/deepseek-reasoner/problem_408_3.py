import mpmath as mp

mp.dps = 15  # Set internal decimal precision

# Calculate 5/3 fraction
fraction_part = mp.mpf(5) / 3

# Compute natural logarithm of 5/3
log_value = mp.log(fraction_part)

# Calculate 2/5 term
subtraction_term = mp.mpf(2) / 5

# Combine components for numerator
numerator = log_value - subtraction_term

# Final result calculation
result = numerator / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))