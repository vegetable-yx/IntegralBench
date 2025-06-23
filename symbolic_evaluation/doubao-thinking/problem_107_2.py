import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the first dilogarithm term: Li_2(1/2)
term1 = mp.polylog(2, 0.5)

# Calculate the second dilogarithm term: Li_2(-1/2)
term2 = mp.polylog(2, -0.5)

# Compute the difference: Li_2(1/2) - Li_2(-1/2)
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))