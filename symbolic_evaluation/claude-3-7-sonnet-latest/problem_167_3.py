import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the natural logarithm of 3
ln3 = mp.log(3)

# Multiply by pi to get the result
result = mp.pi * ln3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))