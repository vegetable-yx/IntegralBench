import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the value of π using mpmath's pi constant
pi_val = mp.pi

# Calculate the fraction π/3
fraction = pi_val / 3

# Compute the natural logarithm of the fraction
log_val = mp.log(fraction)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))