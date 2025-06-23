import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Calculate reciprocal of ln(2)
reciprocal_ln2 = 1 / ln2

# Add constant 3 to the reciprocal
result = 3 + reciprocal_ln2

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))