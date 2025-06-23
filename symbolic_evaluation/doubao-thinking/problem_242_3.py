import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply components to get final result
result = pi_over_2 * zeta_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))