import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute zeta(3) - the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 7/8
result = (7/8) * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))