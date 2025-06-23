import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the natural logarithm of 5
ln5 = mp.log(5)

# Multiply by pi
product = mp.pi * ln5

# Divide by 16 to get the final result
result = product / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))