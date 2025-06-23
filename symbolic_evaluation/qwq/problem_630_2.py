import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Calculate the numerator (π * ln3)
numerator = mp.pi * ln3

# Calculate the denominator (12 * sqrt3)
denominator = 12 * sqrt3

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))