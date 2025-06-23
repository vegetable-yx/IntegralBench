import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by -7/8 coefficient
result = (-7/8) * zeta_3

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))