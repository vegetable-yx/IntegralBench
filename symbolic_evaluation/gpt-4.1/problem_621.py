import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi using mpmath's constant
pi_val = mp.pi

# Compute half of pi
half_pi = pi_val / 2

# Negate to get the final result
result = -half_pi

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))