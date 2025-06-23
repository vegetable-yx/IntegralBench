import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant factor for the numerator
numerator_factor = 3
# Multiply the constant factor by pi to get the numerator
numerator = numerator_factor * mp.pi
# Define the denominator
denominator = 16
# Compute the final result: (3 * pi) / 16
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))