import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Divide by 3 to get the final result
result = zeta_3 / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))