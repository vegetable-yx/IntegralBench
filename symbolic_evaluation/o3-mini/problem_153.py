import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate ln(2)
ln2 = mp.log(2)

# Compute term1: -π/8 * (ln(2))^2
term1 = - (mp.pi / 8) * (ln2 ** 2)

# Compute term2: (1/2) * ln(2) * Catalan's constant (G)
catalan_G = mp.catalan
term2 = (1/2) * ln2 * catalan_G

# Compute dilogarithm terms
Li2_half = mp.polylog(2, 0.5)    # Li_2(1/2)
Li2_neg_half = mp.polylog(2, -0.5)  # Li_2(-1/2)

# Compute term3: (1/8) * [Li_2(1/2) - Li_2(-1/2)]
term3 = (1/8) * (Li2_half - Li2_neg_half)

# Sum all terms
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))