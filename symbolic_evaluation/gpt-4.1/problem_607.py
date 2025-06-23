import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the argument for the logarithm: sqrt(2) + 1
log_arg = sqrt2 + 1

# Compute the natural logarithm of (sqrt(2) + 1)
log_val = mp.log(log_arg)

# Compute pi divided by 2
pi_over_2 = mp.pi / 2

# Multiply to get the final result: (pi/2) * ln(sqrt(2)+1
result = pi_over_2 * log_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))