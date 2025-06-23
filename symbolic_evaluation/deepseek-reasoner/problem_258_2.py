import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential term with exponent -1/4
exp_term = mp.exp(-mp.mpf(1)/4)

# Combine components for final result
result = 2 * sqrt_pi * exp_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))