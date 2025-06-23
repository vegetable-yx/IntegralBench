import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi to get the result
result = mp.pi * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))