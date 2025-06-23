import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the constant pi
pi_value = mp.pi

# Calculate numerator: 19 * pi
numerator = 19 * pi_value

# Calculate denominator: 512
denominator = 512

# Compute the fraction: (19 * pi) / 512
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))