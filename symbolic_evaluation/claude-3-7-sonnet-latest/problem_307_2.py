import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by 2 and by pi
result = 2 * mp.pi * ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))