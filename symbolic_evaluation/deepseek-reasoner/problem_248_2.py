import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 5
ln5 = mp.log(5)

# Multiply the components to get the final result
result = pi_over_4 * ln5

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))