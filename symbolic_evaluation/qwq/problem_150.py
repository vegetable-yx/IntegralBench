import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π raised to the power of 3/2
pi_power = mp.pi ** (3/2)

# Compute the square root of 2 for the denominator
sqrt_denominator = mp.sqrt(2)

# Combine components to get final result
result = pi_power / sqrt_denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))