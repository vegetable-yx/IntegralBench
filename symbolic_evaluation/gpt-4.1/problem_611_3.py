import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: 2 + sqrt(3)
numerator = mp.mpf(2) + mp.sqrt(3)

# Calculate the denominator: sqrt(3)
denominator = mp.sqrt(3)

# Compute the fraction: (2 + sqrt(3)) / sqrt(3)
fraction = numerator / denominator

# Compute the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))