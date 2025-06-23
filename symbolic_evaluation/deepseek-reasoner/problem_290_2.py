import mpmath as mp
mp.dps = 15

# Calculate the numerator: 4 * π
numerator = 4 * mp.pi

# Define the denominator
denominator = 15

# Compute the final result by division
result = numerator / denominator

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))