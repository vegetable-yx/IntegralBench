import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the denominator: 2 * sqrt(2)
denominator = 2 * sqrt2

# Compute the fraction: pi divided by denominator
fraction = mp.pi / denominator

# Apply the negative sign to get the final result
result = -fraction

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))