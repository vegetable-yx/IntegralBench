import mpmath as mp

# Set internal decimal precision to 15 for accurate 10-digit output
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi to get the result
result = mp.pi * ln2

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))