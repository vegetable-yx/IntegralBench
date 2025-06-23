import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the natural logarithm of 3
ln3 = mp.log(3)

# Calculate the constant pi
pi_val = mp.pi

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Numerator: pi * ln(3)
numerator = pi_val * ln3

# Denominator: 12 * sqrt(3)
denominator = 12 * sqrt3

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))