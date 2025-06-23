import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm
ln2_squared = ln2 ** 2

# Multiply by π and divide by 4
result = (mp.pi / 4) * ln2_squared

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))