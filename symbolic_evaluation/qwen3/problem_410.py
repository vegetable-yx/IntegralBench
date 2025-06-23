import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate denominator 2*e
denominator = 2 * mp.e

# Compute final result
result = sqrt_pi / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))