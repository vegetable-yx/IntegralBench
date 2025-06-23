import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply by 2*pi to get the final result
result = 2 * mp.pi * ln2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))