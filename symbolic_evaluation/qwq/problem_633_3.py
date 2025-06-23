import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Compute first term: (7/16) * ζ(3)
term1 = mp.mpf(7)/16 * zeta_3

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute second term: (π²/8) * ln2
term2 = (pi_squared / 8) * ln2

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))