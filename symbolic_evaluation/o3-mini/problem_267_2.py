import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute fundamental constants and logarithmic terms
pi = mp.pi
ln2 = mp.log(2)

# Compute polylogarithm terms at 1/2
Li2_half = mp.polylog(2, 0.5)
Li3_half = mp.polylog(3, 0.5)

# Calculate components of the numerator
term1 = -pi**3
term2 = 12 * pi * ln2**2
term3 = -24 * ln2 * Li2_half
term4 = 48 * Li3_half

# Combine terms to form the numerator
numerator = term1 + term2 + term3 + term4

# Divide by denominator to get final result
result = numerator / 32

# Output result to exactly 10 decimal places
print(mp.nstr(result, n=10))