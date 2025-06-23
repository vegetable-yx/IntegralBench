import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Raise the natural logarithm of 2 to the 4th power
ln2_4 = ln2**4

# Divide by 4 to get the final result
result = ln2_4 / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))