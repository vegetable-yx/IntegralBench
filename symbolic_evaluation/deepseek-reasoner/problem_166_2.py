import mpmath as mp
mp.dps = 15  # Set sufficient precision for internal calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Divide π by 4 to get the final result
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))