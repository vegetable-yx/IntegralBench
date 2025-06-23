import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm
log_argument = 2 + sqrt5

# Calculate natural logarithm of (2 + sqrt(5))
log_value = mp.log(log_argument)

# Multiply by pi and divide by 4
pi_contribution = mp.pi * log_value
result = pi_contribution / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))