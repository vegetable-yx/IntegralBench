import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by -2 to get the final result
result = -2 * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))