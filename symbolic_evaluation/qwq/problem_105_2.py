import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/3
pi_term = mp.pi / 3

# Calculate sqrt(3)/2
sqrt_term = mp.sqrt(3) / 2

# Combine terms for final result
result = pi_term - sqrt_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))