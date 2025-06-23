import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi squared divided by 12
term1 = mp.pi**2 / 12

# Calculate ln(2) and then its square
ln2 = mp.log(2)
ln2_sq = ln2**2
term2 = -6 * ln2_sq

# Calculate 8 * ln(2)
term3 = 8 * ln2

# Constant term
term4 = -4

# Combine all terms
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))