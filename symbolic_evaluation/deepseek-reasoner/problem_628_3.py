import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate each term of the expression separately
term1 = -mp.pi / 8  # First term: -π/8
term2 = -mp.mpf(1)/4  # Second term: -1/4

# Combine terms to get final result
result = term1 + term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))