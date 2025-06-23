import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Li_3(1/2)
li3_positive = mp.polylog(3, 0.5)

# Calculate Li_3(-1/2)
li3_negative = mp.polylog(3, -0.5)

# Compute the difference between the two trilogarithm values
result = li3_positive - li3_negative

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))