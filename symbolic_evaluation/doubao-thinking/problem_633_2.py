import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)
# Calculate the first term: (7/16) * ζ(3)
term1 = (7/16) * zeta_3

# Compute π squared
pi_sq = mp.pi ** 2
# Compute natural logarithm of 2
ln2 = mp.log(2)
# Calculate the second term: (π² / 8) * ln(2)
term2 = (pi_sq / 8) * ln2

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))