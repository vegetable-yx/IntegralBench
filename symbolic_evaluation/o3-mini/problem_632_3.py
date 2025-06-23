import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the natural logarithm of 2
ln2 = mp.log(2)

# Negate the result to get -ln(2)
result = -ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))