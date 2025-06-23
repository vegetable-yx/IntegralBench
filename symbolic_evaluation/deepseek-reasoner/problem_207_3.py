import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π divided by 8
pi_over_8 = mp.pi / 8

# Compute square root of π/8
sqrt_pi_over_8 = mp.sqrt(pi_over_8)

# Apply negative sign to the result
result = -sqrt_pi_over_8

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))