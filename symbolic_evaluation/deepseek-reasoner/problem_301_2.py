import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π using mpmath's constant
pi_val = mp.pi

# Square the π value
pi_squared = mp.power(pi_val, 2)

# Compute the final result by dividing by 16 and applying negative sign
result = -pi_squared / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))