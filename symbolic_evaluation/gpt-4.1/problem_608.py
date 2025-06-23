import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Raise ln(2) to the 4th power
ln2_4 = ln2 ** 4

# Multiply by 1/4 to get the final result
result = ln2_4 / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))