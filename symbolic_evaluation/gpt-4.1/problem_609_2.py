import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Negate the logarithm to get the result
result = -ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))