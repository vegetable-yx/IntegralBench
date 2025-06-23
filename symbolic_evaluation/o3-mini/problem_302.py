import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the first dilogarithm term: Li_2(1/4)
term1 = mp.polylog(2, 0.25)

# Compute the second dilogarithm term: Li_2(-1/4)
term2 = mp.polylog(2, -0.25)

# Combine terms: (term1 - term2) multiplied by 1/2
result = 0.5 * (term1 - term2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))