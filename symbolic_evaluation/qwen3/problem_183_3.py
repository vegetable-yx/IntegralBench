import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate sqrt(5)
sqrt5 = mp.sqrt(5)

# Compute the argument for logarithm: 2 + sqrt(5)
log_arg = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_term = mp.log(log_arg)

# Compute pi/4 multiplier
pi_over_4 = mp.pi / 4

# Calculate final result by multiplying terms
result = pi_over_4 * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))