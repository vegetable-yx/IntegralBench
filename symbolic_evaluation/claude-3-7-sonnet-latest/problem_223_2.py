import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi (mathematical constant π)
pi_val = mp.pi

# Calculate π raised to the power of 3
pi_cubed = mp.power(pi_val, 3)

# Multiply by 2 to get 2π³
result = 2 * pi_cubed

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))