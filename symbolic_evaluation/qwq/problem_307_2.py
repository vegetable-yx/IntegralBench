import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate 1 + sqrt(2)
sqrt_part = mp.sqrt(2)
log_argument = 1 + sqrt_part

# Compute natural logarithm of (1 + sqrt(2))
log_value = mp.log(log_argument)

# Multiply by pi to get final result
pi_value = mp.pi
result = pi_value * log_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))