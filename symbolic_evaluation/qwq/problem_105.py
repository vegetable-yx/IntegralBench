import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π divided by 3
result = pi_value / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))