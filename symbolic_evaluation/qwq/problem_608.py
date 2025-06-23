import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Raise the logarithm result to the 4th power
ln2_pow4 = ln2 ** 4

# Divide by 4 to get final result
result = ln2_pow4 / 4

# Print result with 10 decimal places
print(mp.nstr(result, n=10))