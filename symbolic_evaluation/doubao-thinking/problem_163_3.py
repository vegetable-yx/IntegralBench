import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Multiply by 2 to get the final result
result = 2 * pi_cubed

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))