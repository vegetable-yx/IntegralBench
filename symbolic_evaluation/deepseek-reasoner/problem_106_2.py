import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the first dilogarithm term: Li_2(1/4)
term1 = mp.polylog(2, mp.mpf(1)/4)

# Compute the second dilogarithm term: Li_2(-1/2)
term2 = mp.polylog(2, mp.mpf(-1)/2)

# Combine terms according to the expression
result = term1 - 2 * term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))