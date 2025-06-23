import mpmath as mp
mp.dps = 15

# Calculate the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Apply the negative sign to the result
result = -zeta_3

# Print the final value with 10 decimal precision
print(mp.nstr(result, n=10))