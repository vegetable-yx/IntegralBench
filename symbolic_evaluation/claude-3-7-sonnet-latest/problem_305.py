import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply by 1/2 to get the result
result = 0.5 * ln2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))