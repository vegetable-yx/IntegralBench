import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define common constants and values
ln2 = mp.ln(2)  # Natural logarithm of 2
sqrt2 = mp.sqrt(2)  # Square root of 2
inv_sqrt2 = 1 / sqrt2  # 1/sqrt(2)
neg_inv_sqrt2 = -inv_sqrt2  # -1/sqrt(2)

# Compute polylogarithm differences
# Li_2(1/sqrt(2)) - Li_2(-1/sqrt(2))
Li2_diff = mp.polylog(2, inv_sqrt2) - mp.polylog(2, neg_inv_sqrt2)

# Li_3(1/sqrt(2)) - Li_3(-1/sqrt(2))
Li3_diff = mp.polylog(3, inv_sqrt2) - mp.polylog(3, neg_inv_sqrt2)

# Calculate each term in the expression
term1 = (mp.pi / 4) * (ln2 ** 2)  # π/4 * (ln(2))^2
term2 = 2 * ln2 * Li2_diff  # 2*ln(2)*[Li_2(1/√2) - Li_2(-1/√2)]
term3 = Li3_diff  # Li_3(1/√2) - Li_3(-1/√2)

# Combine terms: term1 + term2 - term3
result = term1 + term2 - term3

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))