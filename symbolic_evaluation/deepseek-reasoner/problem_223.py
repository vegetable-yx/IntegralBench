import mpmath as mp
mp.dps = 15

# Calculate 4πG term using Catalan's constant (G)
term1 = 4 * mp.pi * mp.catalan

# Calculate zeta(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Calculate (7/2)ζ(3) term
term2 = (7/2) * zeta_3

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))