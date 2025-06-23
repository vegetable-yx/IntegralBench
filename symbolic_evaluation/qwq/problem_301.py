import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute π² / 12
pi_sq_over_12 = mp.pi ** 2 / 12

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate each component of the expression
term_4ln2 = 4 * ln2
term_4ln2_sq = 4 * (ln2 ** 2)
constant_term = 2

# Combine all components to get final result
result = pi_sq_over_12 + term_4ln2 - term_4ln2_sq - constant_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))