import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute the result by dividing π by 48
result = pi_value / 48

# Print the final value with 10 decimal precision
print(mp.nstr(result, n=10))