import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Compute π cubed
pi_cubed = pi_val ** 3

# Divide by 12 to get the result
result = pi_cubed / 12

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))