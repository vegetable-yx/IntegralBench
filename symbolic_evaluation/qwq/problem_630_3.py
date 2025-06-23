import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute numerator: π * ln(3)
numerator = pi * ln3

# Compute denominator: 12 * sqrt(3)
denominator = 12 * sqrt3

# Calculate final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))