import mpmath as mp

# Set internal precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Compute π using mpmath's constant
pi_val = mp.pi

# Calculate π cubed
pi_cubed = pi_val ** 3

# Divide by 8 to get the final result
result = pi_cubed / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))