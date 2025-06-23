import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate π/2 component
pi_over_2 = mp.pi / 2

# Compute square root of π/2
sqrt_term = mp.sqrt(pi_over_2)

# Calculate exponent 1/8 using precise division
exponent = mp.mpf(1)/8

# Compute e^(1/8) using precise exponentiation
exp_term = mp.exp(exponent)

# Combine components for final result
result = sqrt_term * exp_term

print(mp.nstr(result, n=10))