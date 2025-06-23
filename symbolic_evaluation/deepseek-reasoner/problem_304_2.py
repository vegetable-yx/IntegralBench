import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate π/16 term
pi_term = mp.pi / 16

# Calculate sqrt(3)/24 term
sqrt3_term = mp.sqrt(3) / 24

# Combine the terms for final result
result = pi_term - sqrt3_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))