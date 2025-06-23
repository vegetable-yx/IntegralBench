import mpmath as mp

# Set internal decimal places for intermediate calculations
mp.dps = 15

# Precompute common constants
sqrt3 = mp.sqrt(3)
atan_sqrt3 = mp.atan(sqrt3)  # arctan(sqrt(3))
atan_inv_sqrt3 = mp.atan(1/sqrt3)  # arctan(1/sqrt(3))

# Compute individual logarithmic terms
ln3 = mp.log(3)
ln4 = mp.log(4)
ln4_over_3 = mp.log(4/3)

# Compute dilogarithm terms
li2_3_4 = mp.polylog(2, 3/4)
li2_1_4 = mp.polylog(2, 1/4)

# Calculate each term of the expression
term1 = (ln3 * atan_sqrt3) / sqrt3
term2 = (ln4 * atan_sqrt3) / 2
term3 = li2_3_4 / 4
term4 = (ln4_over_3 * atan_inv_sqrt3) / 2
term5 = li2_1_4 / 4

# Combine terms to get final result
result = term1 - term2 + term3 + term4 - term5

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))