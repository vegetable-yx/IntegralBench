import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2) using mpmath's square root function
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: 1 + sqrt(2)
log_argument = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_value = mp.log(log_argument)

# Square the logarithm value
log_squared = log_value ** 2

# Compute pi squared
pi_squared = mp.pi ** 2

# Multiply pi squared with the squared logarithm
numerator = pi_squared * log_squared

# Divide by 112 to get the final result
result = numerator / 112

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))