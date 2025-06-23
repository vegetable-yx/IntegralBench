import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 16
result = pi_value / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))