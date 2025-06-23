import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the numerator: 7 * π
numerator = 7 * mp.pi

# Compute the denominator: 3 * √3
denominator = 3 * mp.sqrt(3)

# Calculate the result: (7π) / (3√3)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))