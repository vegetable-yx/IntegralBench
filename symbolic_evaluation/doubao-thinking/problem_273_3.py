import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate sqrt(3)
sqrt3 = mp.sqrt(3)

# Compute the argument for the logarithm
log_arg = (2 + sqrt3) / 4

# Calculate the natural logarithm term
ln_term = mp.log(log_arg)

# Combine all components in the numerator
numerator_part = 4 * sqrt2 - 5 + 6 * ln_term

# Multiply by pi and divide by 72
result = (mp.pi * numerator_part) / 72

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))