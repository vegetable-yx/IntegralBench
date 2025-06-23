import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/4 term
pi_over_4 = mp.pi / 4

# Calculate 1/2 term
half = mp.mpf(1)/2

# Combine terms for final result
result = pi_over_4 - half

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))