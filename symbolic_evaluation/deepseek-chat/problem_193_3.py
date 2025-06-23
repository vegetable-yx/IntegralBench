import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute zeta(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 7/8 to get the final result
result = (mp.mpf(7)/8) * zeta_3

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))