import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply the components to get final result
result = pi_over_4 * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))