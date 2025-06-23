import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the dilogarithm at 1/2
term1 = mp.polylog(2, 0.5)

# Calculate the dilogarithm at -1/2
term2 = mp.polylog(2, -0.5)

# Compute the difference between the two terms
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))