import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate ln(2) using mpmath
ln2 = mp.log(2)

# Compute the first term: (1/2) * ln(2)
term1 = 0.5 * ln2

# Compute the second term: pi/8
term2 = mp.pi / 8

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))