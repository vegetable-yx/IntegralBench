import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Raise ln(2) to the 4th power
ln2_power4 = ln2**4

# Divide by 4 to get final result
result = ln2_power4 / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))