import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Divide by 12 to get final result
result = pi_cubed / 12

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))