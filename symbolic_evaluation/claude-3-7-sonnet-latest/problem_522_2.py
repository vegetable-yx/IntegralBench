import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: sqrt(pi)
numerator = mp.sqrt(mp.pi)

# Calculate the denominator: sqrt(2019)
denominator = mp.sqrt(2019)

# Compute the result: sqrt(pi) / sqrt(2019)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))