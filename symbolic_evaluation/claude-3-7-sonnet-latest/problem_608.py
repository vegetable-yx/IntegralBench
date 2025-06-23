import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Raise ln(2) to the fourth power
ln2_power4 = ln2 ** 4

# Divide by 4 to get the final result
result = ln2_power4 / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))