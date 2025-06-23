import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ln(2) and its square
ln2 = mp.log(2)
ln2_sq = ln2 ** 2

# Compute each term of the expression separately
term1 = -4 * ln2_sq
term2 = 6 * ln2
term3 = -2
term4 = -(mp.pi ** 2) / 12

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))