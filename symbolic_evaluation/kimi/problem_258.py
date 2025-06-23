import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the analytical solution
sqrt_pi = mp.sqrt(mp.pi)  # Compute square root of pi
exp_term = mp.exp(-0.25)  # Compute exponential term e^(-1/4)

# Combine terms for final result
result = 2 * sqrt_pi * exp_term

# Output result with exactly 10 decimal places
print(mp.nstr(result, n=10))