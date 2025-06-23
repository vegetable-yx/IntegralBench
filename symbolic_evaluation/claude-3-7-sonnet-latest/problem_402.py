import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute π divided by 3
pi_over_3 = mp.pi / 3

# Compute the natural logarithm of (π/3)
log_pi_over_3 = mp.log(pi_over_3)

# Multiply the logarithm by 2
result = 2 * log_pi_over_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))