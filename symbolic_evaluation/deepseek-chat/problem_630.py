import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the numerator: pi * ln(3)
numerator = mp.pi * mp.log(3)

# Calculate the denominator: 12 * sqrt(3)
denominator = 12 * mp.sqrt(3)

# Compute the result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))