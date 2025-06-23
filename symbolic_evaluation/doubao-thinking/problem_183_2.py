import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for logarithm: 2 + sqrt(5)
log_argument = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_term = mp.log(log_argument)

# Compute π/4
pi_over_4 = mp.pi / 4

# Multiply components to get final result
result = pi_over_4 * log_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))