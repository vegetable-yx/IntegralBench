import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate zeta(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Multiply by pi to get the final result
result = mp.pi * zeta_3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))