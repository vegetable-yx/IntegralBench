import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/6 term
pi_term = mp.pi / 6

# Calculate sqrt(3)/8 term
sqrt3_term = mp.sqrt(3) / 8

# Combine both terms
result = pi_term + sqrt3_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))