import mpmath as mp

# Set internal decimal places for calculation
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the result to get (ln 2)^2
result = ln2 ** 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))