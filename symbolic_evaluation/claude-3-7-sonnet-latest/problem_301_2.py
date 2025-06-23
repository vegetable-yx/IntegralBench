import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply by 2 and pi
result = -2 * mp.pi * ln2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))