import mpmath as mp
mp.dps = 15

# Calculate the dilogarithm at 1/2
li_half = mp.polylog(2, 0.5)

# Calculate the dilogarithm at -1/2
li_neg_half = mp.polylog(2, -0.5)

# Compute the difference between the two dilogarithm values
result = li_half - li_neg_half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))