import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute 2 divided by sqrt(5)
ratio = 2 / sqrt5

# Compute 1 minus the ratio
inner_expr = 1 - ratio

# Multiply by pi/2
result = (mp.pi / 2) * inner_expr

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))