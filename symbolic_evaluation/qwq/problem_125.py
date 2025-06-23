import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Divide by 8 to get the final result
result = pi_cubed / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))