import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Calculate the dilogarithm function Li₂(1/4)
li2_value = mp.polylog(2, 1/4)

# Multiply the components to get the final result
result = pi_over_2 * li2_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))