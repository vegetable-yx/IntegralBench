import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm
log_argument = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_term = mp.log(log_argument)

# Compute pi/4
pi_over_4 = mp.pi / 4

# Multiply the terms to get final result
result = pi_over_4 * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))