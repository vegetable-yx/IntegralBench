import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate square roots
sqrt_11 = mp.sqrt(11)
sqrt_6 = mp.sqrt(6)

# Compute the argument for the logarithm
log_arg_numerator = sqrt_11 + 1
log_arg = log_arg_numerator / sqrt_6

# Compute the natural logarithm
log_term = mp.log(log_arg)

# Combine the terms: 7*sqrt(11) - 3*sqrt(6) + 6*log_term
combined = 7 * sqrt_11 - 3 * sqrt_6 + 6 * log_term

# Multiply by 1/24 to get the final result
result = combined / 24

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))