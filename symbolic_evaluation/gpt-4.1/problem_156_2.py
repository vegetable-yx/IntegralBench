import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Catalan's constant
G = mp.catalan

# Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute the analytical expression: - (π/2) * G - (7/8) * ζ(3)
pi_over_2 = mp.pi / 2
term1 = -pi_over_2 * G
term2 = - (mp.mpf(7)/8) * zeta3
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))