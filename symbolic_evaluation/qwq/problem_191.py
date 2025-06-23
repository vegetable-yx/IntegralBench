import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute argument for logarithm: 1 + sqrt(2)
log_arg = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(log_arg)

# Square the logarithmic term
log_squared = log_term ** 2

# Calculate pi squared
pi_squared = mp.pi ** 2

# Multiply pi squared with squared logarithmic term
numerator = pi_squared * log_squared

# Divide by 120 to get final result
result = numerator / 120

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))