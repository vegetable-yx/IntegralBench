import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute first term: - (π² / 8) * ln(2)
term1 = -(pi_squared / 8) * ln2

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute second term: (7/16) * ζ(3)
term2 = (7 / 16) * zeta3

# Sum both terms to get final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))