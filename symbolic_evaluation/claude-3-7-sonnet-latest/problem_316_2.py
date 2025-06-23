import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by 2 and by pi
result = 2 * mp.pi * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))