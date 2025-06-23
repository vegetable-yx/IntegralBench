import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/6
term1 = mp.pi / 6

# Calculate sqrt(3)/8
sqrt3 = mp.sqrt(3)
term2 = sqrt3 / 8

# Sum both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))