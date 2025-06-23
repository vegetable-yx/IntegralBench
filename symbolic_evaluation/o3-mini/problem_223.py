import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute ln(2)
ln2 = mp.log(2)

# Compute the first term: (π/2) * [ln(2)]^2
ln2_sq = ln2 ** 2
term1 = (mp.pi / 2) * ln2_sq

# Compute the second term: 4 * Li_2(1/2)
term2 = 4 * mp.polylog(2, 0.5)

# Compute the argument for the third dilogarithm: 1 - 1/sqrt(2)
sqrt2 = mp.sqrt(2)
arg = 1 - 1 / sqrt2

# Compute the third term: -4 * Li_2(1 - 1/sqrt(2))
term3 = -4 * mp.polylog(2, arg)

# Sum all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))