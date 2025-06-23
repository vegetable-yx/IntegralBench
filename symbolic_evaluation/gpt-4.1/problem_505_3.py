import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute π using mpmath's built-in constant
pi_value = mp.pi

# Calculate π/4
result = pi_value / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))