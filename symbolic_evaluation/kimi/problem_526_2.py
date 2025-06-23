import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute natural logarithm of 3
ln3 = mp.log(3)

# Multiply by π and divide by 4
result = (mp.pi * ln3) / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))