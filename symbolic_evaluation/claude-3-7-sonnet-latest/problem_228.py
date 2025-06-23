import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by -7/4 to get the result
result = mp.fmul(-7/4, zeta_3)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))