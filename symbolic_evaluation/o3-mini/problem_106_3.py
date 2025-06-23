import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the first term: Dilogarithm of 1/2
term1 = mp.polylog(2, 0.5)

# Compute the second term: Dilogarithm of -1/2
term2 = mp.polylog(2, -0.5)

# Subtract the terms to get the result
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))