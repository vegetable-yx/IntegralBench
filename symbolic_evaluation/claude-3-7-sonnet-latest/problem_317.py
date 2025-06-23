import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate ln(2)
ln2 = mp.log(2)

# Calculate sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate ln(1 + sqrt(2))
ln_term = mp.log(1 + sqrt2)

# Combine components: -4 * ln(2) * ln(1 + sqrt(2))
result = -4 * ln2 * ln_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))