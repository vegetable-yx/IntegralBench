import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Li_2(1/4)
term1 = mp.polylog(2, 0.25)

# Calculate Li_2(-1/4)
term2 = mp.polylog(2, -0.25)

# Compute the difference between the two polylog terms
difference = term1 - term2

# Multiply by 1/2 to get the final result
result = 0.5 * difference

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))