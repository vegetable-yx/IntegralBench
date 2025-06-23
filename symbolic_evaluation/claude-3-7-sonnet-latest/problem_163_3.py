import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute zeta(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 7 to get the final result
result = 7 * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))