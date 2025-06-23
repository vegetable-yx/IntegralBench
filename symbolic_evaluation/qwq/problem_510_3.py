import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the numerator: 7 * π
numerator = 7 * mp.pi

# Calculate the denominator: 3 * sqrt(3)
denominator = 3 * mp.sqrt(3)

# Compute the final result by dividing numerator by denominator
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))