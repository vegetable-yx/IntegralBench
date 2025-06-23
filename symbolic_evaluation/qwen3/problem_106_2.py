import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the first dilogarithm term: Li_2(1/2)
term1 = mp.polylog(2, 0.5)

# Compute the second dilogarithm term: Li_2(-1/2)
term2 = mp.polylog(2, -0.5)

# Calculate the difference between the two terms
result = term1 - term2

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))