import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant pi divided by 8
pi_over_8 = mp.pi / 8

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply the two components to get the result
result = pi_over_8 * ln2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))