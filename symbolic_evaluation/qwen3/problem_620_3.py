import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/8
pi_over_8 = mp.pi / 8

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply components to get final result
result = pi_over_8 * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))