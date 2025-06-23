import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Compute pi divided by 2
pi_over_2 = mp.pi / 2

# Multiply the two results together
result = pi_over_2 * ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))