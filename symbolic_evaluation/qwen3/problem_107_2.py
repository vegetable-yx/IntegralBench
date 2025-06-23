import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the first dilogarithm term: Li_2(1/2)
term1 = mp.polylog(2, 0.5)

# Compute the second dilogarithm term: Li_2(-1/2)
term2 = mp.polylog(2, -0.5)

# Combine the results: Li_2(1/2) - Li_2(-1/2)
result = term1 - term2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))