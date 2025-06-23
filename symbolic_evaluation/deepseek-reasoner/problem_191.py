import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Divide by 512 to get the final result
result = pi_cubed / 512

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))