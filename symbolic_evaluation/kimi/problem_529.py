import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Assign the constant value: negative pi
result = -mp.pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))