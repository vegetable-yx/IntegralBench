import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define constants and intermediate values
ln2 = mp.log(2)          # Natural logarithm of 2
sqrt2 = mp.sqrt(2)        # Square root of 2
inv_sqrt2 = 1 / sqrt2     # 1/sqrt(2)

# Compute the first term: (π/4) * (ln(2))^2
term1 = (mp.pi / 4) * (ln2 ** 2)

# Compute the trilogarithm differences: Li3(1/sqrt(2)) - Li3(-1/sqrt(2))
li3_pos = mp.polylog(3, inv_sqrt2)    # Li3(1/sqrt(2))
li3_neg = mp.polylog(3, -inv_sqrt2)   # Li3(-1/sqrt(2))
term2 = 2 * (li3_pos - li3_neg)       # 2 * (Li3_pos - Li3_neg)

# Sum the terms for the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))