import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π squared
pi_squared = mp.pi ** 2

# Compute the numerator (27 * π²)
numerator = 27 * pi_squared

# Define the denominator
denominator = 512

# Calculate the final result
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))