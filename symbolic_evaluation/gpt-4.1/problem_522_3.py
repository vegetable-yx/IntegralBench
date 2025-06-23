import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate numerator: sqrt(pi)
numerator = mp.sqrt(mp.pi)

# Calculate denominator: sqrt(2019)
denominator = mp.sqrt(2019)

# Compute the result: sqrt(pi) / sqrt(2019)
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))