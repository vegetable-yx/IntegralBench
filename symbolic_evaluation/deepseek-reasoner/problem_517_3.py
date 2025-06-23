import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate sqrt(π/2)
sqrt_pi_over_2 = mp.sqrt(mp.pi / 2)

# Calculate e^(1/8)
exp_term = mp.exp(mp.mpf(1)/8)

# Multiply components for final result
result = sqrt_pi_over_2 * exp_term

# Print with 10 decimal precision
print(mp.nstr(result, n=10))