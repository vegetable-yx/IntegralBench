import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π cubed
pi_cubed = pi_val ** 3

# Divide by 64 to get the final result
result = pi_cubed / 64

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))