import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute each term of the expression separately

# Term 1: π³ / 96
term1 = mp.power(mp.pi, 3) / 96

# Term 2: (π / 16) * (ln(2))²
ln2 = mp.log(2)  # Natural logarithm of 2
ln2_sq = ln2 * ln2  # (ln(2))^2
term2 = (mp.pi / 16) * ln2_sq

# Term 3: (1/8) * [Li₂(1/2) - Li₂(-1/2)]
# Compute dilogarithms at x=1/2 and x=-1/2
li2_half = mp.polylog(2, 0.5)
li2_minus_half = mp.polylog(2, -0.5)
diff_li2 = li2_half - li2_minus_half  # Difference of dilogarithms
term3 = (1/8) * diff_li2

# Combine all terms: result = term1 - term2 + term3
result = term1 - term2 + term3

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))