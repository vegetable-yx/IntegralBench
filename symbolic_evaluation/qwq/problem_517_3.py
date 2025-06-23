import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^(1/8)
exp_term = mp.exp(mp.mpf(1)/8)

# Calculate sqrt(pi/2)
sqrt_pi_over_2 = mp.sqrt(mp.pi/2)

# Multiply components to get final result
result = exp_term * sqrt_pi_over_2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))