import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate e^(1/8) component
exponent = mp.mpf(1)/8
exp_component = mp.exp(exponent)

# Calculate sqrt(pi/2) component
pi_half = mp.pi / 2
sqrt_component = mp.sqrt(pi_half)

# Combine components for final result
result = exp_component * sqrt_component

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))