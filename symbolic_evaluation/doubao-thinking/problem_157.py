import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate exponential term e^(-1/4)
exp_term = mp.exp(-mp.mpf(1)/4)

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Combine components for final result
result = 12 * exp_term * sqrt_pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))