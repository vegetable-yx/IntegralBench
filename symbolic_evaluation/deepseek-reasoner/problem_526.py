import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 3
ln_3 = mp.log(3)

# Multiply the two components to get final result
result = pi_over_4 * ln_3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))