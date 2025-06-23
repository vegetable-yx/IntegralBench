import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π/2
pi_over_2 = pi_value / 2

# Calculate the final result 2 - π/2
result = 2 - pi_over_2

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))