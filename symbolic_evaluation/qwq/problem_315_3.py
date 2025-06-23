import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate ζ(3) using the Riemann zeta function
zeta_3 = mp.zeta(3)

# Compute the final result
result = -zeta_3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))