import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π cubed
pi_cubed = pi_value ** 3

# Divide by 16 to get the final result
result = pi_cubed / 16

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))