import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Calculate 49 times ζ(3)
term1 = 49 * zeta3

# Compute the rational constant 175/4
term2 = mp.mpf(175) / 4

# Combine results: 49ζ(3) - 175/4
result = term1 - term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))