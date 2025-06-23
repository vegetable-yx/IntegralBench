import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the constant: negative pi
result = -mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))