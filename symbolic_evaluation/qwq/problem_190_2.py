import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) for the logarithmic argument
sqrt2 = mp.sqrt(2)

# Compute the argument for the natural logarithm
log_arg = 1 + sqrt2

# Calculate the natural logarithm term
log_term = mp.log(log_arg)

# Square the logarithmic term
log_squared = log_term ** 2

# Calculate pi squared
pi_squared = mp.pi ** 2

# Combine all components according to the formula
result = (pi_squared / 128) * log_squared

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))