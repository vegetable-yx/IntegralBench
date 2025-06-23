import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate Li_2(1/2) using polylog function
li_2_positive = mp.polylog(2, 0.5)

# Calculate Li_2(-1/2) using polylog function
li_2_negative = mp.polylog(2, -0.5)

# Compute the difference between the two dilogarithm values
result = li_2_positive - li_2_negative

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))