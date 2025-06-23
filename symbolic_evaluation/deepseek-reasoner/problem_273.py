import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Compute ln(1 + sqrt(2))
ln_term = mp.log(1 + sqrt2)

# Compute ln(2)
ln2 = mp.log(2)

# Calculate 4*ln(1 + sqrt(2))
term1 = 4 * ln_term

# Calculate 2*ln(2)
term2 = 2 * ln2

# Combine all terms: 4*ln_term - 2*ln2 - 1
combined_terms = term1 - term2 - 1

# Multiply by pi/24 to get final result
result = (mp.pi / 24) * combined_terms

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))