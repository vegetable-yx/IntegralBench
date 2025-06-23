import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply the result by 8
result = 8 * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))