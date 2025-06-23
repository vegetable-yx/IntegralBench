import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm
ln2_squared = ln2 ** 2

# Compute final result: 1 - (ln2)^2
result = 1 - ln2_squared

# Print result to 10 decimal places
print(mp.nstr(result, n=10))