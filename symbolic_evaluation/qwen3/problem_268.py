import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Compute π/8
pi_over_8 = pi / 8

# Calculate ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply components to get final result
result = pi_over_8 * zeta_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))