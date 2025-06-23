import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
log_argument = 1 + sqrt2

# Calculate natural logarithm of (1 + sqrt(2))
log_term = mp.log(log_argument)

# Multiply by pi to get the final result
result = mp.pi * log_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))