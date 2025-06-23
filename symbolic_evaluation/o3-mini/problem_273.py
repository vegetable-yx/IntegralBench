import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: (1 + sqrt(2)) / 2
log_arg = (1 + sqrt2) / 2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Multiply the logarithm by 6
log_term = 6 * log_val

# Compute 4 times the square root of 2
sqrt_term = 4 * sqrt2

# Combine the terms: 4*sqrt(2) - 5 + 6*log_value
numerator_inner = sqrt_term - 5 + log_term

# Multiply by pi and divide by 72
result = (mp.pi * numerator_inner) / 72

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))