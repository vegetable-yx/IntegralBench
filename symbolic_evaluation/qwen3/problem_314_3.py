import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate Li_3(-1/2)
term1 = mp.polylog(3, -0.5)

# Calculate Li_3(1/2)
term2 = mp.polylog(3, 0.5)

# Compute the difference between the two polylogarithm terms
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))