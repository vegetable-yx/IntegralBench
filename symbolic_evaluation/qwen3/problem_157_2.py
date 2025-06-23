import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential term e^(-1/4)
exp_term = mp.exp(-mp.mpf(1)/4)

# Combine components for final result
result = 12 * sqrt_pi * exp_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))