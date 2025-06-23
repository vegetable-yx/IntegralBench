import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Divide π by 3
pi_over_3 = pi_val / 3

# Compute natural logarithm of (π/3)
log_val = mp.log(pi_over_3)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))