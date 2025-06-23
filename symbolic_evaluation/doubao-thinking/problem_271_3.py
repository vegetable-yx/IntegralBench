import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 19 * pi
numerator = 19 * mp.pi

# Calculate the denominator: 512
denominator = 512

# Compute the result: (19 * pi) / 512
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))