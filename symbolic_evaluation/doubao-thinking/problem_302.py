import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the first dilogarithm term
term1 = mp.polylog(2, 1/4)

# Calculate the second dilogarithm term with negative argument
term2 = mp.polylog(2, -1/4)

# Compute the final result by combining terms
result = 0.5 * (term1 - term2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))