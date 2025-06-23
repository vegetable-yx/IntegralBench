import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Multiply by pi to compute the result
result = mp.pi * ln2_val

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))