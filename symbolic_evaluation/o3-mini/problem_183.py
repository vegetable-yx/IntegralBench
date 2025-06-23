import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the argument for the logarithm: 2 + sqrt(5)
log_arg = 2 + sqrt5

# Compute the natural logarithm of (2 + sqrt(5))
ln_val = mp.log(log_arg)

# Calculate pi/4
pi_over_4 = mp.pi / 4

# Multiply pi/4 by the logarithm value
result = pi_over_4 * ln_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))