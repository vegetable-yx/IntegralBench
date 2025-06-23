import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi (using mpmath constant)
pi_val = mp.pi

# Compute pi cubed
pi_cubed = pi_val ** 3

# Define the denominator
denominator = 12

# Compute the result: π³ / 12
result = pi_cubed / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))