import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Calculate 2 times the natural logarithm of 2
two_ln2 = 2 * ln2

# Subtract 2*ln(2) from 1
factor = 1 - two_ln2

# Multiply the result by pi
result = mp.pi * factor

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))