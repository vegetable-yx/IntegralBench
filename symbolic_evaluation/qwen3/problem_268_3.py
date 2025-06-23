import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π divided by 8
pi_over_8 = mp.pi / 8

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply the two components to get the final result
result = pi_over_8 * zeta_3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))