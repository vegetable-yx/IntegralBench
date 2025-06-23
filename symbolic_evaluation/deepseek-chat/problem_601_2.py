import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi to get the result
result = mp.pi * ln2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))