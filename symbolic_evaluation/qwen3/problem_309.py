import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Calculate denominator (8 * sqrt(2))
denominator = 8 * sqrt_two

# Compute final result by dividing π² by the denominator
result = pi_sq / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))