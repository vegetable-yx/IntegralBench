import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Catalan constant (G)
G = mp.catalan

# Calculate the natural logarithm of 2
ln2 = mp.ln(2)

# Calculate pi
pi = mp.pi

# Compute term: (pi * ln(2)) / 8
term1 = (pi * ln2) / 8

# Compute term: G / 8
term2 = G / 8

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))