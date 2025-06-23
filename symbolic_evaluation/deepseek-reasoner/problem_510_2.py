import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the square root of 3
sqrt_3 = mp.sqrt(3)

# Compute the denominator 3*sqrt(3)
denominator = 3 * sqrt_3

# Calculate the final result (7π)/denominator
result = (7 * mp.pi) / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))