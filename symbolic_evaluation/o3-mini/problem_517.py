import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi/2
pi_over_2 = mp.pi / 2

# Compute the square root of (pi/2)
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Calculate e^(1/8)
exp_term = mp.exp(mp.mpf(1)/8)

# Multiply the two components
result = sqrt_pi_over_2 * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))