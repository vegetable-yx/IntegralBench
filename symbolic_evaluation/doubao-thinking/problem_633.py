import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute first term: -(π²/8) * ln2
term1 = -(pi_squared / 8) * ln2

# Calculate Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute second term: (7/16) * ζ(3)
term2 = (7 / 16) * zeta3

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))