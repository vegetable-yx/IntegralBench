import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Base of natural logarithm
e_val = mp.e

# Compute powers of e
e2 = e_val**2
e3 = e_val**3
e4 = e_val**4

# Compute terms in the expression
term1 = 3
term2 = 2 * e_val
term3 = 2 * e2
term4 = 2 * e3
term5 = -e4

# Combine all terms
result = term1 + term2 + term3 + term4 + term5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))