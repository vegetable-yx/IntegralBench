import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute the difference (ln2 - 1)
difference = ln2 - 1

# Multiply by 2 to get final result
result = 2 * difference

# Print result with 10 decimal places
print(mp.nstr(result, n=10))