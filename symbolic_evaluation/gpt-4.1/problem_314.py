import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by the rational coefficient -7/8
result = -7 * zeta_3 / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))