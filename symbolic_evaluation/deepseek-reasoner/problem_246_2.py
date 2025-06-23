import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the rational coefficient
coefficient = mp.mpf(10395) / 16

# Calculate π squared
pi_squared = mp.pi ** 2

# Combine components for final result
result = coefficient * pi_squared

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))