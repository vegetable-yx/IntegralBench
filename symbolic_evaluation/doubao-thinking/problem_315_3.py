import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate ζ(3) using the Riemann zeta function
zeta_3 = mp.zeta(3)

# Multiply by 1/4 to get the final result
result = zeta_3 / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))