import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute π using mpmath's constant
pi_val = mp.pi

# Calculate π raised to the power of 3
pi_cubed = pi_val ** 3

# Divide the result by 384
result = pi_cubed / 384

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))