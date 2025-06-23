import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute the value of pi divided by 3
pi_over_3 = pi_val / 3

# Compute the natural logarithm of (pi/3)
log_val = mp.log(pi_over_3)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))