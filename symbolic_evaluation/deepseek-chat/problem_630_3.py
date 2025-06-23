import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi)
pi_val = mp.pi

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute numerator: π * ln(3)
numerator = pi_val * ln3

# Compute denominator: 12 * √3
denominator = 12 * sqrt3

# Compute final result: (π * ln(3)) / (12 * √3)
result = numerator / denominator

# Print result rounded to 10 decimal places
print(mp.nstr(result, n=10))