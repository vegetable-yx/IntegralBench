import mpmath as mp
mp.dps = 15  # Set decimal precision for all calculations

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute 4 times ln2 term
linear_term = 4 * ln2

# Compute 4 times (ln2 squared) term
quadratic_term = 4 * (ln2 ** 2)

# Combine all components for final result
result = 2 + linear_term - quadratic_term

# Output final value with 10 decimal precision
print(mp.nstr(result, n=10))