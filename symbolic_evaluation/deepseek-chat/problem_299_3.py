import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply by -2 to get the result
result = -2 * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))