import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute zeta(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Compute pi divided by 8
pi_over_8 = mp.pi / 8

# Multiply to get the result
result = pi_over_8 * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))