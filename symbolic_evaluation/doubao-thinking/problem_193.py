import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate fundamental constants
pi = mp.pi
ln2 = mp.log(2)

# Compute each term of the expression separately
term1 = (pi ** 4) / 144
term2 = (pi ** 2) * (ln2 ** 2) / 24
term3 = (ln2 ** 4) / 6

# Combine terms according to the formula
result = term1 - term2 + term3

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))