import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Calculate Li₂(1/2)
li_1_half = mp.polylog(2, 0.5)

# Calculate Li₂(-1/2)
li_minus_half = mp.polylog(2, -0.5)

# Compute the difference between the two dilogarithm values
result = li_1_half - li_minus_half

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))