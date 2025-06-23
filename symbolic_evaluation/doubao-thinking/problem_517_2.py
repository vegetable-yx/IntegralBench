import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute square root of (π/2)
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Compute e^(1/8)
exp_term = mp.exp(1/8)

# Multiply the two components
result = sqrt_pi_over_2 * exp_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))