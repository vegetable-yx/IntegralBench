import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Compute the fraction ln(2) / ln(3)
fraction = ln2 / ln3

# Subtract the fraction from 2 to get the final result
result = 2 - fraction

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))