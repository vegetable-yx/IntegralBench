import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/6 term
term1 = mp.pi / 6

# Calculate sqrt(3)/8 term
sqrt3 = mp.sqrt(3)
term2 = sqrt3 / 8

# Combine both terms
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))