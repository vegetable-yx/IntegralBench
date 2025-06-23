import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Divide by 96 to get the final result
result = pi_cubed / 96

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))