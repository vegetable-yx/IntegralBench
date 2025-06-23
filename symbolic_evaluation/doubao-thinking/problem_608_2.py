import mpmath as mp

# Set decimal precision for calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Raise the logarithm to the 4th power
ln2_power4 = ln2**4

# Multiply by 1/4 to get the final result
result = ln2_power4 / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))