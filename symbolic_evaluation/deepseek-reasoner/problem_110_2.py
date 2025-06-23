import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π by 2 division
result = pi_value / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))