import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/24 term
pi_term = mp.pi / 24

# Calculate sqrt(3)/16 term
sqrt3_term = mp.sqrt(3) / 16

# Combine terms for final result
result = pi_term - sqrt3_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))