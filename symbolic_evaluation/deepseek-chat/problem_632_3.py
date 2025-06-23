import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithms for the constants
ln3 = mp.log(3)  # Natural logarithm of 3
ln2 = mp.log(2)  # Natural logarithm of 2

# Compute the first term: (2/3) * ln(3)
term1 = (2 * ln3) / 3

# Compute the second term: (4/3) * ln(2)
term2 = (4 * ln2) / 3

# Combine the terms: result = term1 - term2
result = term1 - term2

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))