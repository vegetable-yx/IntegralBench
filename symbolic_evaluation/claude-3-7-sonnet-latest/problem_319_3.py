import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: pi minus 2
numerator = mp.pi - 2

# Calculate the denominator
denominator = 2

# Compute the result: (pi - 2) / 2
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))