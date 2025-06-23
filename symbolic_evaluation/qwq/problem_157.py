import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the exponential term e^(-1/4)
exp_term = mp.exp(-mp.mpf(1)/4)

# Multiply all components together: 24 * sqrt(pi) * e^(-1/4)
result = 24 * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))