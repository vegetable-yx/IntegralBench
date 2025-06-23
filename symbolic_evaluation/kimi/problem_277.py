import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate sqrt(2*pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Calculate e^1 - 1
exp_term = mp.exp(1) - 1

# Combine terms for final result
result = (sqrt_2pi * exp_term) / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))