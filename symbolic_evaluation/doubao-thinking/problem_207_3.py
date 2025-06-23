import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π divided by 8
pi_over_8 = mp.pi / 8

# Compute the square root of π/8
sqrt_pi_over_8 = mp.sqrt(pi_over_8)

# Apply the negative sign to get the final result
result = -sqrt_pi_over_8

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))