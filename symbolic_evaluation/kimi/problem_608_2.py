import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Raise ln(2) to the 4th power
ln2_power4 = ln2**4

# Multiply by -47 to get the final result
result = -47 * ln2_power4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))