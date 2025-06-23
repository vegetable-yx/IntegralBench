import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Compute the fraction π/3
fraction = pi_val / 3

# Compute the natural logarithm of the fraction
log_val = mp.log(fraction)

# Multiply the logarithm by 2
result = 2 * log_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))