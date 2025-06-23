import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 7/2 to get the final result
result = (7 / 2) * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))