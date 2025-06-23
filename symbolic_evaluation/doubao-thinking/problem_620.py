import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute pi divided by 8
pi_over_8 = mp.pi / 8

# Multiply the two components to get the result
result = pi_over_8 * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))