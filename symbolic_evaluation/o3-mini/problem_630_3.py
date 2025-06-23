import mpmath as mp

# Set internal decimal precision to 15 for sufficient accuracy
mp.dps = 15

# Calculate the numerator: pi * ln(3)
numerator = mp.pi * mp.log(3)

# Calculate the denominator: 12 * sqrt(3)
denominator = 12 * mp.sqrt(3)

# Compute the final result: (pi * ln(3)) / (12 * sqrt(3))
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))