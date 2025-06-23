import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/2
pi_over_2 = mp.pi / 2

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: 1 + sqrt(2)
log_arg = 1 + sqrt2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Multiply pi/2 by the logarithm value
result = pi_over_2 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))