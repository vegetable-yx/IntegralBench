import mpmath as mp
mp.dps = 15

# Calculate ζ(3) using the Riemann zeta function
zeta_3 = mp.zeta(3)

# Multiply by 7 to get the final result
result = 7 * zeta_3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))