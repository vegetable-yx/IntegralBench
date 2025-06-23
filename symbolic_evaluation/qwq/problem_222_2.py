import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 3π using mpmath's pi
pi_value = mp.pi  # Get mpmath's high-precision π constant
result = 3 * pi_value  # Multiply π by 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))