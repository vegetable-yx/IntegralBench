import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Compute the numerator: 2 * ln(2) - 1
numerator = 2 * ln2 - 1

# Divide the numerator by 8 to get the final result
result = numerator / 8

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))