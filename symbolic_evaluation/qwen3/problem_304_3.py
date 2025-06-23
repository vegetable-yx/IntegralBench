import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/32 component
term1 = mp.pi / 32

# Calculate sqrt(3)/24 component
term2 = mp.sqrt(3) / 24

# Combine components for final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))