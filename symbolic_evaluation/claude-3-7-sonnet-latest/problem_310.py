import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate natural logarithm of 4
ln4 = mp.log(4)

# Multiply by pi to get the final result
result = mp.pi * ln4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))