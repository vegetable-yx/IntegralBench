import mpmath as mp
mp.dps = 15  # Set decimal precision

# Calculate e^(1/8)
exp_term = mp.exp(mp.mpf(1)/8)

# Calculate square root of (π/2)
sqrt_term = mp.sqrt(mp.pi/2)

# Combine components for final result
result = exp_term * sqrt_term

print(mp.nstr(result, n=10))