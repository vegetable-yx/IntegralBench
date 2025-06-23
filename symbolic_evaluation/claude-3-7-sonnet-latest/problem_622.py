import mpmath as mp

# Set the internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the numerator: 6 + π
numerator = 6 + mp.pi

# Calculate the denominator
denominator = 32

# Compute the result: (6 + π) / 32
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))