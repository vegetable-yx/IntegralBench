import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Multiply by 3 to get the numerator
numerator = 3 * pi_cubed

# Divide by 32 to get the final result
result = numerator / 32

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))