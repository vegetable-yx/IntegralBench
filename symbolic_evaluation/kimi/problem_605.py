import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 8
result = pi_value / 8

# Print the result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))