import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Calculate π cubed
pi_cubed = pi_val ** 3

# Divide π cubed by 8 to get the result
result = pi_cubed / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))