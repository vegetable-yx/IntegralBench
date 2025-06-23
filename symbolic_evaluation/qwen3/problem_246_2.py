import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the rational coefficient 315/8
coefficient = mp.mpf(315) / 8

# Compute the Riemann zeta function at 9
zeta_9 = mp.zeta(9)

# Multiply coefficient with zeta(9) to get final result
result = coefficient * zeta_9

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))