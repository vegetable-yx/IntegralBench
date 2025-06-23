import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential component e^(-1/4)
exp_component = mp.exp(-mp.mpf(1)/4)

# Combine components for final result
result = 12 * sqrt_pi * exp_component

# Print with 10 decimal precision
print(mp.nstr(result, n=10))