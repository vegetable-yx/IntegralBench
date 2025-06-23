import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 2 * sqrt(pi)
numerator = 2 * mp.sqrt(mp.pi)

# Calculate the denominator: sqrt(2019)
denominator = mp.sqrt(2019)

# Compute the result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))