import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Calculate the final result using the coefficient -13/8
result = (-13/8) * zeta_3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))