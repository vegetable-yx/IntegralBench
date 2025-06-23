import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the dilogarithm at 1/2
term1 = mp.polylog(2, 0.5)

# Calculate the dilogarithm at -1/2
term2 = mp.polylog(2, -0.5)

# Compute the difference: Li₂(1/2) - Li₂(-1/2)
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))