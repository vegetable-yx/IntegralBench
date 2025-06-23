import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute pi/3
pi_over_3 = mp.pi / 3

# Compute natural logarithm of pi_over_3
log_val = mp.log(pi_over_3)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))