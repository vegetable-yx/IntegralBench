import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 4 and by pi
result = 4 * mp.pi * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))