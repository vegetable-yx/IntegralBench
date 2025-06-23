import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: -π/8
term1 = -mp.pi / 8

# Calculate the second term: -1/4
term2 = -mp.mpf(1)/4

# Combine both terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))