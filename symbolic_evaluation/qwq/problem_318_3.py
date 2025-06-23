import mpmath as mp
mp.dps = 15

# Calculate each component of the expression
term1 = mp.sqrt(2) / 3
term2 = mp.asin(mp.sqrt(3)/3)
term3 = mp.ellipe(1/2)

# Combine components for final result
result = term1 * (term2 + term3)

# Print with 10 decimal precision
print(mp.nstr(result, n=10))