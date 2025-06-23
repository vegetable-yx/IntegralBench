import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first dilogarithm term: Li_2(1/2)
term1 = mp.polylog(2, 0.5)

# Calculate the second dilogarithm term: Li_2(1/4)
term2 = mp.polylog(2, 0.25)

# Combine the terms according to the expression: 2 * term1 - (1/2) * term2
result = 2 * term1 - (1/2) * term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))