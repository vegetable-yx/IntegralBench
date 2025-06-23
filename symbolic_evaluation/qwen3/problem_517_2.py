import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute square root of π/2
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Calculate exponential of 1/8
exp_term = mp.exp(mp.mpf(1)/8)

# Multiply components to get final result
result = sqrt_pi_over_2 * exp_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))