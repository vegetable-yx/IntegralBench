import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the natural logarithm term ln(1 + sqrt(2))
sqrt2 = mp.sqrt(2)
ln_term = mp.log(1 + sqrt2)

# Compute the squared logarithm term (ln(1+sqrt(2)))^2
ln_sq = ln_term ** 2

# Calculate each component of the expression
term1 = 3 * ln_sq
term2 = 2 * sqrt2 * ln_term
combined_terms = term1 - term2 + 1

# Multiply by pi/8 to get the final result
result = (mp.pi / 8) * combined_terms

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))