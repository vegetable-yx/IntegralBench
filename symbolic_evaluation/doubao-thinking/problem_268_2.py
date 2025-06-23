import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate pi divided by 8
pi_over_8 = mp.pi / 8

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply the components to get final result
result = pi_over_8 * zeta_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))