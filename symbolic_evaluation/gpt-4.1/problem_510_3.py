import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the numerator: 7 * π
numerator = 7 * mp.pi

# Calculate the denominator: 3 * √3
denominator = 3 * mp.sqrt(3)

# Compute the result: (7π) / (3√3)
result = numerator / denominator

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))