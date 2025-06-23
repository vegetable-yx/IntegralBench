import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the numerator: -2 * pi
numerator = -2 * mp.pi

# Compute the denominator: sqrt(5) + 5
denominator = mp.sqrt(5) + 5

# Calculate the final result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))