import mpmath as mp

# Set internal decimal places for calculation to 15
mp.dps = 15

# Calculate the numerator: sqrt(6) - 1
numerator = mp.sqrt(6) - 1

# Calculate the denominator: sqrt(12)
denominator = mp.sqrt(12)

# Compute the fraction: (sqrt(6)-1)/sqrt(12)
fraction = numerator / denominator

# Multiply the fraction by pi
result = mp.pi * fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))