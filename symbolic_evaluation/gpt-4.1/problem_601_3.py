import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi
result = mp.pi * ln2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))