import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Compute π using mpmath's constant
pi_value = mp.pi

# Calculate π cubed
pi_cubed = pi_value ** 3

# Divide by 96 to get the final result
result = pi_cubed / 96

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))