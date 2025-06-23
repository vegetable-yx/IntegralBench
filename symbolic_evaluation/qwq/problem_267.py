import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Compute π cubed
pi_cubed = pi_val ** 3

# Divide by 305 to get the final result
result = pi_cubed / 305

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))