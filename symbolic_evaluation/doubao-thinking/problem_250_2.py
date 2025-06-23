import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/√2
term1 = mp.pi / mp.sqrt(2)

# Calculate π/2
term2 = mp.pi / 2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))