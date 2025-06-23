import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define the numerator
numerator = mp.mpf(2)

# Calculate the denominator: 3 * pi
denominator = mp.mpf(3) * mp.pi

# Compute the result: 2 / (3 * pi)
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))