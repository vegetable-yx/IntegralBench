import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate e^(1/8) using mpmath exponential
exp_term = mp.exp(mp.mpf(1)/8)

# Calculate square root of (π/2)
sqrt_term = mp.sqrt(mp.pi/2)

# Combine results for final answer
result = exp_term * sqrt_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))