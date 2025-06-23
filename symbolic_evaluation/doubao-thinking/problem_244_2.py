import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Square the calculated π value
pi_squared = mp.power(pi_value, 2)

# Define the denominator
denominator = 144

# Compute the final result by division
result = pi_squared / denominator

# Print result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))