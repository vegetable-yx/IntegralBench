import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Raise the logarithm to the fourth power
ln2_4 = ln2**4

# Multiply by 153
numerator = 153 * ln2_4

# Divide by 4 and apply the negative sign
result = -numerator / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))