import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the natural logarithm of 3
ln3 = mp.log(3)

# Multiply by pi and divide by 4 to get the result
result = (mp.pi * ln3) / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))