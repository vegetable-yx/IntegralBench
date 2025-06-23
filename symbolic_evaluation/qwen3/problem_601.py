import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by the constant pi
result = mp.pi * ln2

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))