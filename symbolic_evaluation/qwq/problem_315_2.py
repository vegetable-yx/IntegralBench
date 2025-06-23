import mpmath as mp
mp.dps = 15

# Calculate zeta(3) using mpmath's zeta function
zeta_3 = mp.zeta(3)

# Multiply by -7/8 coefficient
result = (-7/8) * zeta_3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))