import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute square root of π/2
sqrt_pi_over_2 = mp.sqrt(pi_over_2)

# Apply negative sign to the result
result = -sqrt_pi_over_2

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))