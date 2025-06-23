import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 2 to get the final result
result = 2 * zeta_3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))